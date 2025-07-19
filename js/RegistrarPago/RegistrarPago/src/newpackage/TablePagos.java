/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package newpackage;

import javax.swing.table.DefaultTableModel;

public class TablePagos {
    public static DefaultTableModel modeloPagos = new DefaultTableModel();

    static {
        modeloPagos.addColumn("Id");
        modeloPagos.addColumn("Dni");
        modeloPagos.addColumn("Mes");
        modeloPagos.addColumn("Saldo");
        modeloPagos.addColumn("Fecha");
        modeloPagos.addColumn("N° de Recibo");
        modeloPagos.addColumn("Entidad Financiera");
        modeloPagos.addColumn("Tipo de Pago");
    }
}
