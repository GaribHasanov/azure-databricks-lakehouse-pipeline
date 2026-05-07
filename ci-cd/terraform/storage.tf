resource "azurerm_storage_account" "adls" {
  name                     = "retaillakehousesa"
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  is_hns_enabled = true
}
