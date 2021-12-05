import javax.swing.JOptionPane;

public class BaseConvert {
  public static void main(String[] args) {
	  
    //BigInteger[] totalVal = new BigInteger[0];      //read pg 137

	String baseIn = JOptionPane.showInputDialog("Base In:");
    String baseOut = JOptionPane.showInputDialog("Base Out:");
    String num = JOptionPane.showInputDialog("Number:");
    
    Base conv = new Base(baseIn, baseOut, num);
    System.out.println(conv.getOutput());
    
  }
 }