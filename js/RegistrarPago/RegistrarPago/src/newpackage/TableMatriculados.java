/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package newpackage;

import javax.swing.table.DefaultTableModel;

public class TableMatriculados {
    public static DefaultTableModel modeloMatriculados = new DefaultTableModel();

    static {
        modeloMatriculados.addColumn("Id");
        modeloMatriculados.addColumn("Nombres");
        modeloMatriculados.addColumn("Apellidos");
        modeloMatriculados.addColumn("Dni");
        modeloMatriculados.addColumn("Sexo");
        modeloMatriculados.addColumn("Domicilio");
        modeloMatriculados.addColumn("IE de Procedencia");
        modeloMatriculados.addColumn("Saldo");
        modeloMatriculados.addColumn("Fecha");
        modeloMatriculados.addColumn("N° de Recibo");
        modeloMatriculados.addColumn("Entidad Financiera");
    }
}
