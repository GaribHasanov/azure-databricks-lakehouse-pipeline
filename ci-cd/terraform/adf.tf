resource "azurerm_data_factory" "adf" {
  name                = "retail-adf"
  location            = var.location
  resource_group_name = var.resource_group_name
}
