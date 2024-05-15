provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "myResourceGroup"
  location = "East US"
}

resource "azurerm_virtual_machine_scale_set" "example" {
  name                = "myScaleSet"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku                 = "Standard_DS1_v2"

  # Other VMSS configuration (image, networking, etc.)

  tags = {
    environment = "dev"
  }
}
