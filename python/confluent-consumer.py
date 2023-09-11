from confluent_kafka import Consumer, KafkaException 

conf = {'bootstrap.servers': "localhost:19093",
        'group.id': "foobar",
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': 'false',
        'security.protocol': 'SSL',
        'ssl.ca.location': '/Users/jleong/docker-containers/python-ssl-selfsigned-test/ca.pem'}


def assignment_callback(consumer, partitions):
    for p in partitions:
        print(f'Assigned to {p.topic}, partition {p.partition}')


if __name__ == '__main__':
    consumer = Consumer(conf)
    consumer.subscribe(['test-topic'], on_assign=assignment_callback)
    print(f'Subscribed to topic successfully!')
    try:
        while True:
            event = consumer.poll(1.0)
            if event is None:
                continue
            if event.error():
                raise KafkaException(event.error())
            else:
                val = event.value().decode('utf8')
                partition = event.partition()
                print(f'Received: {val} from partition {partition}    ')
                # consumer.commit(event)
    except KeyboardInterrupt:
        print('Canceled by user.')
    finally:
        consumer.close()




