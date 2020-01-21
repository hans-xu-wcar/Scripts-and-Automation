Some Notes for adding custom metrics for CloudWatch monitoring from ACloudGuru

# Test Custom Metrics   
`/home/ec2-user/aws-scripts-mon/mon-put-instance-data.pl --mem-util --verify --verbose`
# Send metrics to CloudWatch   
`/home/ec2-user/aws-scripts-mon/mon-put-instance-data.pl --mem-util --mem-used --mem-avail`
# Cron Job for Detailed Monitoring - Write to crontab
*/1 * * * * root /home/ec2-user/aws-scripts-mon/mon-put-instance-data.pl --mem-util --mem-used --mem-avail
