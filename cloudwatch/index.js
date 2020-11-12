
const AWS = require('aws-sdk');

const credentials = new AWS.Credentials(process.env.AWS_ACCESS_KEY_ID, process.env.AWS_SECRET_ACCESS_KEY, process.env.AWS_SESSION_TOKEN)

//var credentials = new AWS.EnvironmentCredentials('AWS');
//console.log(process.env.AWS_REGION);

AWS.config.update({
    credentials: credentials,
    region: process.env.AWS_REGION
});

// Create CloudWatch service object
var cw = new AWS.CloudWatch({ apiVersion: '2010-08-01' });

//'INSUFFICIENT_DATA', 'ALARM', 'OK'
// cw.describeAlarms({ StateValue: 'OK' }, function (err, data) {
//     if (err) {
//         console.log("Error", err);
//     } else {
//         // List the names of all current alarms in the console
//         data.MetricAlarms.forEach(function (item, index, array) {
//             console.log(item);
//         });
//     }
// });


cw.describeAlarms({ AlarmNames: ['test'] }, function (err, data) {
    if (err) {
        console.log("Error", err);
    } else {
        console.log("Success", data);
    }
});

