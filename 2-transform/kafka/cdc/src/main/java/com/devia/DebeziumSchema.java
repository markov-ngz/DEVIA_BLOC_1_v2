package com.devia;
import java.util.List;

class DebeziumSchema {
    private String type;
    private List<Field> fields;
    private boolean optional;
    private String name;
    private int version;

    // Getters and setters
    public String getType() { return type; }
    public void setType(String type) { this.type = type; }
    public List<Field> getFields() { return fields; }
    public void setFields(List<Field> fields) { this.fields = fields; }
    public boolean isOptional() { return optional; }
    public void setOptional(boolean optional) { this.optional = optional; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getVersion() { return version; }
    public void setVersion(int version) { this.version = version; }
}