package com.devia;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

/**
 * Hello world!
 */ 
public class App {
     private static final Logger Logger = LogManager.getLogger(App.class);
    public static void main(String[] args) {
        System.setProperty("log4j.configurationFile","./log4j2.xml");
    }
}
