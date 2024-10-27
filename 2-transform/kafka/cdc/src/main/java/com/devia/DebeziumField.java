package com.devia;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.List;

class Field {
    private String type;
    private boolean optional;
    private String name;
    private String field;
    private List<Field> fields;
    private String version;
    private DebeziumParameters parameters;
    @JsonProperty("default")
    private String defaultValue;

    // Getters and setters
    public String getType() { return type; }
    public void setType(String type) { this.type = type; }
    public boolean isOptional() { return optional; }
    public void setOptional(boolean optional) { this.optional = optional; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getField() { return field; }
    public void setField(String field) { this.field = field; }
    public List<Field> getFields() { return fields; }
    public void setFields(List<Field> fields) { this.fields = fields; }
    public String getVersion() { return version; }
    public void setVersion(String version) { this.version = version; }
    public DebeziumParameters getParameters() { return parameters; }
    public void setParameters(DebeziumParameters parameters) { this.parameters = parameters; }
    public String getDefaultValue() { return defaultValue; }
    public void setDefaultValue(String defaultValue) { this.defaultValue = defaultValue; }
}
