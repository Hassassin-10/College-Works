import java.net.*;

public class UDPServer {
    public static void main(String[] args) throws Exception {
        DatagramSocket ds = new DatagramSocket(3000);
        byte[] buf = new byte[1024];

        System.out.println("Server is running and waiting for UDP messages...");

        while (true) {
            DatagramPacket dp = new DatagramPacket(buf, buf.length);
            ds.receive(dp);

            String msg = new String(dp.getData(), 0, dp.getLength());
            System.out.println("Received message: " + msg);
        }
    }
}
