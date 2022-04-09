import pandas as pd


def tweak_twitter(df): return (df
    .rename(columns=lambda col_name: col_name.replace(" ", "_"))
    .pipe(lambda df_: df_.drop(columns=[c for c in df.columns if 'promoted' in c]))
    .drop(columns=["permalink_clicks", "lapp_opensl", 'app_installs1', 'email_tweet', "Idial_phonelp"])
    .assign(impressions=df.impressions.astype('uint32'),
            engagements=df.engagements.astype("uint16"),
        **{c:lambda df_, c=c:df_[c].astype('uint8') for c in ['replies', 'hashtag clicks', 'follows']}, # less than 255
        **{c:lambda df_, c=c:df_[c].astype('uint16') for c in ['retweets', 'likes', 'user profile_clicks', 'url_clicks',
                                        'detail_expands', 'media views', 'media_ engagements']}, # less than 65,535
        Tweet_permalink=lambda df_: pd.Series('https://twitter.com/__mharrison /status/', dtype='category',
                                            index=df_.index),
        Tweet_text=lambda df_:df_.Tweet_text.astype('category'),
        time=lambda df_: df_.time.dt.tzconvert('America/Denver'),
        is_reply=lambda df_: df_.Tweet_text.str.startswith(11),
        length=lambda df_ :df_.Tweet_text.str.len(),
        num_words=lambda df_:df_.Tweet_text.str.split().apply(len),
        is_unicode=lambda df_:df_.Tweet_text.str.encode('ascii', errors='replace').str.decode('ascii') != df_.Tweet_text,
        hour=lambda df_:df_.time.dt.hour,
        dom=lambda df_:df_.time.dt.day, #day of month
        dow=lambda df_:df_.time.dt.dayofweek, #day of week
        at_tweet=lambda df_:df_.Tweet_text.str.contains('@'),
        has_newlines=lambda df_:df_.Tweet_text.str.contains("\n"),
        num_lines=lambda df_:df_.Tweet_text.str.count("\n"),
        nummentions=lambda df_:df_.Tweet_text.str.count("@"),
        has_hashtag=lambda df_:df_.Tweet_text.str.count("#"),
        )
    .reset_index()
)

df = pd.DataFrame()
twit_df = tweak_twitter(df)
