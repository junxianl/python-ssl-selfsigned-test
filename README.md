# python-ssl-selfsigned-test
testing out python ssl module

# steps to reproduce:

```
docker-compose up -d

kafka-topics --bootstrap-server localhost:19092 --create --topic test-topic
kafka-console-producer --bootstrap-server localhost:19092 --topic test-topic
```
produce some data

```cd python```

modify the two python files to point to the correct directory for the SSL ca.pem file - depending on where your PWD is


get dependencies

```
pip3 install confluent-kafka
pip3 install kafka-python
pip3 install pykafka
```


run consumer

```python3 kafka-consumer.py```

observe output

```python3 confluent-consumer.py```

observe error
