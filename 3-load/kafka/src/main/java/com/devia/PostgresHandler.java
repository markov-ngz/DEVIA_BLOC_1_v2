package com.devia;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class PostgresHandler {
    private Connection connection;
    private String url;
    private String user;
    private String password;

    public PostgresHandler(String url, String user, String password) {
        this.url = url;
        this.user = user;
        this.password = password;
    }

    public void connect() throws SQLException {
        if (connection == null || connection.isClosed()) {
            connection = DriverManager.getConnection(url, user, password);
        }
    }

    public void disconnect() throws SQLException {
        if (connection != null && !connection.isClosed()) {
            connection.close();
        }
    }

    public ResultSet executeQuery(String query) throws SQLException {
        connect();
        PreparedStatement stmt = connection.prepareStatement(query);
        return stmt.executeQuery();
    }

    public int executeUpdate(String query) throws SQLException {
        connect();
        PreparedStatement stmt = connection.prepareStatement(query);
        return stmt.executeUpdate();
    }
    
    public boolean isConnected() throws SQLException {
        return connection != null && !connection.isClosed();
    }
}
