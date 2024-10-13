package com.devia ;
import java.util.Properties;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;


public class IngestionProducer {

    Properties properties = new Properties() ;

    String serializer="org.apache.kafka.common.serialization.StringSerializer" ;

    String topic ; 
    
    String bootstrap_server ;
    
    Producer<String, String> producer;

    public  IngestionProducer(String topic,String bootstrap_server){
        this.topic = topic ;
        this.bootstrap_server = bootstrap_server ;  
        this.setProperties();

        this.producer = new KafkaProducer<String, String>(this.properties) ; 
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

}
