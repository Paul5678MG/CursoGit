/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package newpackage;

import javax.swing.table.DefaultTableModel;

public class TableEstudiantes {
    public static DefaultTableModel modeloEstudiantes = new DefaultTableModel();

    static {
        modeloEstudiantes.addColumn("Id");
        modeloEstudiantes.addColumn("Nombres");
        modeloEstudiantes.addColumn("Apellidos");
        modeloEstudiantes.addColumn("Dni");
        modeloEstudiantes.addColumn("Sexo");
        modeloEstudiantes.addColumn("Domicilio");
        modeloEstudiantes.addColumn("IE de Procedencia");
    }
}
