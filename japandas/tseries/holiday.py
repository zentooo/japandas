#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

import datetime
import os

import pandas as pd
import pandas.tseries.holiday as holiday

current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, 'data', 'holidays.pkl')
tse_data_path = os.path.join(current_dir, 'data', 'tseholidays.pkl')


def _read_rules(path):
    if os.path.exists(path):
        rules - pd.read_pickle(path)
    elif __name__ != '__main__':
        raise ImportError("Unable to load '{0}'".format(path))
    else:
        rules = None
    return rules


rules = _read_rules(data_path)
tse_rules = _read_rules(tse_data_path)


class JapaneseHolidayCalendar(holiday.AbstractHolidayCalendar):
    rules = rules


class TSEHolidayCalendar(holiday.AbstractHolidayCalendar):
    rules = tse_rules


# register to pandas factory
holiday.register(JapaneseHolidayCalendar)
holiday.register(TSEHolidayCalendar)


if __name__ == '__main__':

    # Procedure
    # cd japandas/tseries
    # Open https://github.com/holiday-jp/holiday_jp
    # Download holidays.yaml to data directory
    # python holiday.py

    import yaml

    def to_pickle(dates, path):
        rules = []
        keys = sorted(compat.iterkeys(dates))
        for dt in keys:
            name = dates[dt]
            h = holiday.Holiday(
                name, dt.year, month=dt.month, day=dt.day)
            rules.append(h)

        with open(path, mode='wb') as w:
            compat.cPickle.dump(rules, w, protocol=2)
            print('pickled {0} data'.format(len(dates)))

    with open(os.path.join('data', 'holidays.yml'), mode='rb') as f:
        data = yaml.load(f)
    # JapaneseHolidayCalendar
    to_pickle(data, data_path)

    tse_data = data.copy()
    for y in range(1970, 2031):
        for m, d in [(1, 1), (1, 2), (1, 3), (12, 31)]:
            dt = datetime.date(y, m, d)
            if dt not in tse_data:
                tse_data[dt] = {'name': '年末年始休業日', 'date': dt}

    # TSEHolidayCalendar
    to_pickle(tse_data, tse_data_path)
