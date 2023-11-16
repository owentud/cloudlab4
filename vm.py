from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

def main():
    client = ComputeManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="bcf9608c-2e05-436e-93f7-cbf7063ba4aa",
    )

    response = client.virtual_machines.begin_create_or_update(
        resource_group_name="owen",
        vm_name="{vm-name}",
        parameters={
            "location": "westeurope",
            "properties": {
                "hardwareProfile": {"vmSize": "Standard_D1_v2"},
                "networkProfile": {
                    "networkInterfaces": [
                        {
                            "id": "/subscriptions/bcf9608c-2e05-436e-93f7-cbf7063ba4aa/resourceGroups/NOSA.VM_group/providers/Microsoft.Network/networkInterfaces/nic4",
                            "properties": {"primary": True},
                        }
                    ]
                },
                "osProfile": {
                    "adminUsername": "sysowen",
                    "computerName": "vm4",
                },
                "storageProfile": {
                    "osDisk": {
                        "caching": "ReadWrite",
                        "createOption": "FromImage",
                        "image": {
                            "uri": "http://{existing-storage-account-name}.blob.core.windows.net/{existing-container-name}/{existing-generalized-os-image-blob-name}.vhd"
                        },
                        "name": "myVMosdisk",
                        "osType": "Windows",
                        "vhd": {
                            "uri": "http://{existing-storage-account-name}.blob.core.windows.net/{existing-container-name}/myDisk.vhd"
                        },
                    }
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2023-07-01/examples/virtualMachineExamples/VirtualMachine_Create_CustomImageVmFromAnUnmanagedGeneralizedOsImage.json
if __name__ == "__main__":
    main()