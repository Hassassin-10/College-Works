import java.util.Scanner;

public class Leaky {

    public static int bucketSize = 1000;
    public static int outputRate = 100;

    public static void sendPacket(int pktSize){
        if(pktSize > bucketSize){
            System.out.println("Bucket OverFlow");
        }
        else{
            while (pktSize > outputRate) {
                System.out.println(outputRate+"bytes of packet is sent");
                pktSize=pktSize-outputRate;
            }
            System.out.println(pktSize+"bytes of packet is sent");
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the no of packets: ");
        int numpackets = scanner.nextInt();
        if(numpackets > 0){
            for(int i=1;i<=numpackets;i++){
                System.out.println("Enter the packet "+i+" size: ");
                int pktSize = scanner.nextInt();
                sendPacket(pktSize);
            }
        }
        else{
            System.out.println("No Packets to Send");
        }
    }
}