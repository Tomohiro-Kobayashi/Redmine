# -*- coding: utf-8 -*-

import twint
from datetime import datetime, timedelta

today = datetime.today()

c = twint.Config()
c.Search = 'ネップリ 番号'
# c.Limit = 10
c.Store_csv = True
c.Output = "twitter_result.csv"
c.Since = "2022-01-01"
c.Until = "2022-11-23"

twint.run.Search(c)

