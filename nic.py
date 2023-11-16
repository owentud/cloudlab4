from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="bcf9608c-2e05-436e-93f7-cbf7063ba4aa",
    )

    response = client.network_interfaces.begin_create_or_update(
        resource_group_name="owen",
        network_interface_name="nic4",
        parameters={
            "location": "westeurope",
            "properties": {
                "ipConfigurations": [
                    {
                        "name": "ipconfig1",
                        "properties": {
                            "publicIPAddress": {
                                "id": "/subscriptions/bcf9608c-2e05-436e-93f7-cbf7063ba4aa/resourceGroups/owen/providers/Microsoft.Network/publicIPAddresses/ip4"
                            },
                            "subnet": {
                                "id": "/subscriptions/bcf9608c-2e05-436e-93f7-cbf7063ba4aa/resourceGroups/owen/providers/Microsoft.Network/virtualNetworks/owen-vnet/subnets/default"
                            },
                        },
                    }
                ],
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2023-05-01/examples/NetworkInterfaceCreate.json
if __name__ == "__main__":
    main()