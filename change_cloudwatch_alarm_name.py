import sys
import boto


def rename_alarm(alarm_name, new_alarm_name):
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

    alarm.name = new_alarm_name
    conn.update_alarm(alarm)

    # update actually creates a new alarm because the name has changed, so
    # we have to manually delete the old one
    get_alarm().delete()

if __name__ == '__main__':
    alarm_name, new_alarm_name = sys.argv[1:3]

    rename_alarm(alarm_name, new_alarm_name)
    
# ~/.boto
#[Credentials]
#aws_access_key_id = 
#aws_secret_access_key = 
#[Boto]
#cloudwatch_region_name = ap-northeast-1
#cloudwatch_region_endpoint = monitoring.ap-northeast-1.amazonaws.com
