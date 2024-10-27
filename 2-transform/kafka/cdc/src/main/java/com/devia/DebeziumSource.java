package com.devia;

import com.fasterxml.jackson.annotation.JsonProperty;

public class DebeziumSource {
    private String version;
    private String connector;
    private String name;
    @JsonProperty("ts_ms")
    private Long tsMs;
    private String snapshot;
    private String db;
    private String sequence;
    private String schema;
    private String table;
    private Long txId;
    private Long lsn;
    private Long xmin;

    // Getters and setters
    public String getVersion() { return version; }
    public void setVersion(String version) { this.version = version; }
    public String getConnector() { return connector; }
    public void setConnector(String connector) { this.connector = connector; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public Long getTsMs() { return tsMs; }
    public void setTsMs(Long tsMs) { this.tsMs = tsMs; }
    public String getSnapshot() { return snapshot; }
    public void setSnapshot(String snapshot) { this.snapshot = snapshot; }
    public String getDb() { return db; }
    public void setDb(String db) { this.db = db; }
    public String getSequence() { return sequence; }
    public void setSequence(String sequence) { this.sequence = sequence; }
    public String getSchema() { return schema; }
    public void setSchema(String schema) { this.schema = schema; }
    public String getTable() { return table; }
    public void setTable(String table) { this.table = table; }
    public Long getTxId() { return txId; }
    public void setTxId(Long txId) { this.txId = txId; }
    public Long getLsn() { return lsn; }
    public void setLsn(Long lsn) { this.lsn = lsn; }
    public Long getXmin() { return xmin; }
    public void setXmin(Long xmin) { this.xmin = xmin; }
}
