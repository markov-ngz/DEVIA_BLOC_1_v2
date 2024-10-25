package com.devia ;
import java.time.Duration;
import java.util.Arrays;
import java.util.Properties;
import java.util.UUID;

import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringDeserializer;


public class KafkaHandler {

    private Properties properties = new Properties() ;

    private String serializer="org.apache.kafka.common.serialization.StringSerializer" ;

    private String topic ; 
    
    private String bootstrap_server ;
    
    public Producer<String, String> producer;

    public KafkaConsumer<String, String> consumer ;  

    public  KafkaHandler(){

    }
    public void setProducer(String topic, String bootstrap_server){
        this.topic = topic ;
        this.bootstrap_server = bootstrap_server ;  
        this.setProperties();

        this.producer = new KafkaProducer<String, String>(this.properties) ; 
    }

    
    public void setConsumer(String topic, String bootstrap_server){
        this.topic = topic ;
        this.bootstrap_server = bootstrap_server ;  
        this.setProperties();
        this.properties.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG,"earliest");
        
        this.properties.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        this.properties.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        // as this is for testing, generate a random group id
        this.properties.put(ConsumerConfig.GROUP_ID_CONFIG, UUID.randomUUID().toString()); 

        this.consumer = new KafkaConsumer<>(this.properties);
    }

    private void setProperties(){

        // bootstrap server address
        this.properties.put("bootstrap.servers", this.bootstrap_server) ;
        //Specify buffer size in config
        this.properties.put("batch.size", 16384);
        //Reduce the no of requests less than 0   
        this.properties.put("linger.ms", 1);
        //The buffer.memory controls the total amount of memory available to the producer for buffering.   
        this.properties.put("buffer.memory", 33554432);
        //Format Serialization
        this.properties.put("key.serializer",this.serializer);
        this.properties.put("value.serializer", this.serializer);
    }

    public void writeMessage(String key, String value) {
        ProducerRecord<String,String> record =  new ProducerRecord<String,String>(this.topic, key, value) ;  
        this.producer.send(record) ; 
        producer.flush();
    }

    public void readMessage(){
        this.consumer.subscribe(Arrays.asList(this.topic));
        ConsumerRecords<String, String> records = consumer.poll(Duration.ofSeconds(50));

        for (ConsumerRecord<String, String> record : records) {
            System.out.println(record.value());
        }
    }
    
}
