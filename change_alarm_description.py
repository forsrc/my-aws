#coding=utf-8

import sys
import boto

reload(sys)
sys.setdefaultencoding('utf8')

def update_alarm(alarm_name):
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

    print("this is " + alarm.name)
    alarm.description = "this is " + alarm.name
    conn.update_alarm(alarm)



    # update actually creates a new alarm because the name has changed, so
    # we have to manually delete the old one
if __name__ == '__main__':
    alarm_name, = sys.argv[1:2]

    update_alarm(alarm_name)
