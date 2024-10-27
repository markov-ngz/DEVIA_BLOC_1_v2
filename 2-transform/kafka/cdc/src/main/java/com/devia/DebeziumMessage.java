package com.devia;

public class DebeziumMessage {
    private DebeziumSchema schema;
    private DebeziumPayload payload;

    // Getters and setters
    public DebeziumSchema getSchema() { return schema; }
    public void setSchema(DebeziumSchema schema) { this.schema = schema; }
    public DebeziumPayload getPayload() { return payload; }
    public void setPayload(DebeziumPayload payload) { this.payload = payload; }
}
