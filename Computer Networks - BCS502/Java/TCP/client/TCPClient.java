package client;
import java.io.*;
import java.net.*;
import java.util.Scanner;

public class TCPClient {

    public static void main(String[] args) throws IOException,InterruptedException {
        DataOutputStream out;
        DataInputStream in;
        Scanner scanner = new Scanner(System.in);
        
        Socket socket = new Socket("127.0.0.1",6000);
        System.out.println("Client Connected to Server");
        System.out.println("Enter the filename to request");
        String filename = scanner.nextLine();
        in = new DataInputStream(socket.getInputStream());
        out = new DataOutputStream(socket.getOutputStream());
        out.writeUTF(filename);
        String fileContent = in.readUTF();
        if(fileContent.length() > 0){
            System.out.println(fileContent);
        }
        else{
            System.out.println("FILE IS EMPTY");
        }
    }
}