/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package newpackage;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
/**
 *
 * @author PAUL
 */
public class ConexionSQL {
    private static final String URL = "jdbc:sqlserver://PAUL\\SQLEXPRESS01:1433;databaseName=RegistroPagos;encrypt=true;trustServerCertificate=true";
    private static final String USER = "ColegioAngeles";
    private static final String PASSWORD = "pagos234";

    public static Connection getConexion() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }
}

