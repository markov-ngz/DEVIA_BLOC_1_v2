package com.devia; 

import java.net.http.HttpClient;
import java.net.http.HttpHeaders;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpRequest.BodyPublishers;
import java.util.List;
import java.util.Map;
import java.net.URI;

public class ApiHandler {
    
    private String apiKey ; 

    public ApiHandler() {
        this.apiKey = System.getenv("API_KEY") ; 
        HttpClient client = HttpClient.newHttpClient() ; 
    }
    public void sendPOST(String url, Object payload){
        HttpRequest request = HttpRequest.newBuilder()
        .POST(BodyPublishers.ofString("Example"))
        .header("Authorization", String.format("Bearer %s",this.apiKey))
        .header("Content-Type", "application/json")
        .uri(URI.create(url))
        .build(); 
    }
}
