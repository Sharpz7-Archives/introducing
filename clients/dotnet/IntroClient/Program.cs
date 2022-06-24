using System.Threading.Tasks;
using Grpc.Net.Client;
using IntroClient;

// The port number must match the port of the gRPC server.
using var channel = GrpcChannel.ForAddress("http://localhost:50051");

var client = new Card.CardClient(channel);

var reply = await client.get_cardAsync(
                  new request { NoOfCards = 1 });

Console.WriteLine("Greeting: " + reply);
// Console.WriteLine("Press any key to exit...");
// Console.ReadKey();
