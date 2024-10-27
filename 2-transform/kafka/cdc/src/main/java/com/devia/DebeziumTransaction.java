package com.devia;

import com.fasterxml.jackson.annotation.JsonProperty;

public class DebeziumTransaction {
    private String id;
    @JsonProperty("total_order")
    private Long totalOrder;
    @JsonProperty("data_collection_order")
    private Long dataCollectionOrder;

    // Getters and setters
    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public Long getTotalOrder() { return totalOrder; }
    public void setTotalOrder(Long totalOrder) { this.totalOrder = totalOrder; }
    public Long getDataCollectionOrder() { return dataCollectionOrder; }
    public void setDataCollectionOrder(Long dataCollectionOrder) { this.dataCollectionOrder = dataCollectionOrder; }
}
