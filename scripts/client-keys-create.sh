keytool -keystore ../client-creds/kafka.client.truststore.pkcs12 \
    -alias CARoot \
    -import \
    -file ../ca.crt \
    -storepass confluent  \
    -noprompt \
    -storetype PKCS12
