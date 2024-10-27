package com.devia;

import com.fasterxml.jackson.annotation.JsonProperty;

public class DebeziumPayload {
    private TranslationValue before;
    private TranslationValue after;
    private Source source;
    private String op;
    @JsonProperty("ts_ms")
    private Long tsMs;
    private Transaction transaction;

    // Getters and setters
    public TranslationValue getBefore() { return before; }
    public void setBefore(TranslationValue before) { this.before = before; }
    public TranslationValue getAfter() { return after; }
    public void setAfter(TranslationValue after) { this.after = after; }
    public Source getSource() { return source; }
    public void setSource(Source source) { this.source = source; }
    public String getOp() { return op; }
    public void setOp(String op) { this.op = op; }
    public Long getTsMs() { return tsMs; }
    public void setTsMs(Long tsMs) { this.tsMs = tsMs; }
    public Transaction getTransaction() { return transaction; }
    public void setTransaction(Transaction transaction) { this.transaction = transaction; }
}
 