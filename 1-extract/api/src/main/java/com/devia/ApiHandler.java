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
    private HttpClient client = HttpClient.newHttpClient() ; 

    public ApiHandler() {
        this.apiKey = System.getenv("API_KEY") ; 
        
    }
    public HttpResponse<String> sendPOST(String url, String payload){
        HttpRequest request = HttpRequest.newBuilder()
        .POST(BodyPublishers.ofString(payload))
        .header("Authorization", String.format("Bearer %s",this.apiKey))
        .header("Content-Type", "application/json")
        .header("x-wait-for-model", "true") // Specific Huggingface api
        .uri(URI.create(url))
        .build(); 

        try {
            // genericType that holds a string 
            HttpResponse<String> response = this.client.send(request, HttpResponse.BodyHandlers.ofString());
            return response ; 
        }catch(Exception e){
            throw new Error(e);
        }
    }
}
