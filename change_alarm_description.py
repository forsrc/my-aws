#coding=utf-8

import sys
import boto

reload(sys)
sys.setdefaultencoding('utf8')

def update_alarm(alarm_name, description):
    conn = boto.connect_cloudwatch()

    def get_alarm():
        alarms = conn.describe_alarms(alarm_names=[alarm_name])
        if not alarms:
            raise Exception("Alarm '%s' not found" % alarm_name)
        return alarms[0]

    alarm = get_alarm()

    # work around boto comparison serialization issue
    # https://github.com/boto/boto/issues/1311
    alarm.comparison = alarm._cmp_map.get(alarm.comparison)

    print(alarm.name + " : " + alarm.description)
    alarm.description = "this is " + alarm.name
    conn.update_alarm(alarm)

if __name__ == '__main__':
    alarm_name, description = sys.argv[1:3]

    update_alarm(alarm_name, description)
