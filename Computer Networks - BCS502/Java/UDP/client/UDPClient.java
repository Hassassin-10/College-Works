import java.net.*;
import java.util.Scanner;

public class UDPClient {

    public static void main(String[] args) throws Exception {
        System.out.println("Sender");
        DatagramSocket ds = new DatagramSocket();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the message : ");
        while (true) {
            String msg = scanner.nextLine();
            InetAddress ip = InetAddress.getByName("127.0.0.1");
            DatagramPacket dp = new DatagramPacket(msg.getBytes(),msg.length(),ip,3000);
            ds.send(dp);
        }
    }
}