from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="bcf9608c-2e05-436e-93f7-cbf7063ba4aa",
    )

    response = client.public_ip_addresses.begin_create_or_update(
        resource_group_name="owen",
        public_ip_address_name="ip4",
        parameters={"location": "westeurope"},
    ).result()
    print(response)

if __name__ == "__main__":
    main()