from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer(bootstrap_servers=['localhost:19093'],
                             security_protocol='SSL',
                             ssl_cafile='/Users/jleong/docker-containers/python-ssl-selfsigned-test/ca.pem',
                             auto_offset_reset='earliest',
                             enable_auto_commit=False)
    consumer.subscribe(['test-topic'])
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                              message.offset, message.key,
                                              message.value))

