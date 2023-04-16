#!/usr/bin/env bash

# %%

# load gcp into temporal bq table
function gcs_to_bq_temp() {
    datasource="$1"
    country="gbr"
    datefmt="202302"
    bucket="carto-ext-prov-echo-analytics"
    bucket_trim=$(echo ${bucket} | tr '-' '_')
    bq_dataset="data-observatory-ops:do_raw"

    from_gcs="gs://${bucket}/${datasource}/${gbr}/${datefmt}*.parquet"
    to_bq_table="${bq_dataset}.${bucket_trim}_${gbr}_${datasource}_${datefmt}_parquet"

    bq load --replace --source_format PARQUET ${to_bq_table} ${from_gcs}

    echo Loaded
    echo ${to}
}

# Usage:
# gcs_to_bq_temp "places_activity"
# gcs_to_bq_temp "places_activity_shapes"
# gcs_to_bq_temp "places_shapes"
# gcs_to_bq_temp "places"


function schema_from_sheet() {
    sheet_url="$1"
    fmt=".loc[:, ['column_name', 'db_type']].rename({'column_name': 'name', 'db_type': 'type'}, axis=1).to_json(orient='records')"
    out_file="/tmp/gs_schema_$(uuidgen).json"
    gsheet $sheet_url --fmt=$fmt > /tmp/raw_gs_schema.json
    cat /tmp/raw_gs_schema.json | tr -d '\n' | python3 -m json.tool > $out_file
    echo $out_file
}

function schema_from_bq() {
    out_file="/tmp/bq_schema_$(uuidgen).json"
    bq_table="$1"
    bq show --schema "${bq_table}" > /tmp/raw_bq_schema.json
    cat /tmp/raw_bq_schema.json | python3 -m json.tool | sed '/"mode":/d' | sed 's/\(\s\+"type":.*\),$/\1/g' > $out_file
    echo $out_file

}

function schema_diff() {
    editor=$EDITOR
    sch_bq=$(schema_from_bq "$1")
    sch_sheet=$(schema_from_sheet "$2")
    echo $sch_sheet
    echo $sch_bq
    $editor -d $sch_sheet $sch_bq +'nmap gq :qa!<cr>'
}

# %%

# list files
gsutil ls -r 'gs://carto-ext-prov-echo-analytics' | grep 2023 | grep 00.parquet

# out:
# gs://carto-ext-prov-echo-analytics/places/gbr/202302-000000000000.parquet
# gs://carto-ext-prov-echo-analytics/places_activity/gbr/202302-000000000000.parquet
# gs://carto-ext-prov-echo-analytics/places_activity_shapes/gbr/202302-000000000000.parquet
# gs://carto-ext-prov-echo-analytics/places_shapes/gbr/202302-000000000000.parquet

# %%

schema_from_sheet "https://docs.google.com/spreadsheets/d/1CKVmngn5TJTTSWqaJHrxvMOSj25h5WZrkhOA2bY9hJ8"
schema_from_bq "data-observatory-ops:do_raw.echo_gbr_places_202302_parquet"

schema_diff
cat /tmp/gs_schema.json
cat /tmp/bq_schema.json


# find layout urls
gsheet "https://docs.google.com/spreadsheets/d/1wLI0oe_zqqxoESTrcv0mjeR8escv9kznczVn-NwdVFk/edit#gid=1799284994" --tab Layouts --fmt ".tail().to_string()"

# %%

schema_diff "data-observatory-ops:do_raw.echo_gbr_places_202302_parquet" "https://docs.google.com/spreadsheets/d/1CKVmngn5TJTTSWqaJHrxvMOSj25h5WZrkhOA2bY9hJ8"
schema_diff "data-observatory-ops:do_raw.echo_gbr_places_shapes_202302_parquet" "https://docs.google.com/spreadsheets/d/1f9Uq_PCcBC5XZFVcCfZreRIsWQY8poH8KcG42roqsic"
schema_diff "data-observatory-ops:do_raw.echo_gbr_places_activity_202302_parquet" "https://docs.google.com/spreadsheets/d/1vb6UeoDSVDDrHPXqPFUG79afz1me_oYRA-B1HKOgjQ4"
schema_diff "data-observatory-ops:do_raw.echo_gbr_places_activity_shapes_202302_parquet" "https://docs.google.com/spreadsheets/d/1EPRHfLudAPOhPjYeCh8CrD_ry202ofcJa9I3cQYM1d4"
