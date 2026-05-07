terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# ---------------------------
# Resource Group
# ---------------------------
resource "azurerm_resource_group" "rg" {
  name     = "lakehouse-rg"
  location = "West Europe"
}

# ---------------------------
# Storage Account (ADLS Gen2)
# ---------------------------
resource "azurerm_storage_account" "adls" {
  name                     = "lakehousestorageacct"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled           = true
}

# ---------------------------
# Data Factory
# ---------------------------
resource "azurerm_data_factory" "adf" {
  name                = "lakehouse-adf"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

# ---------------------------
# Databricks Workspace
# ---------------------------
resource "azurerm_databricks_workspace" "dbw" {
  name                = "lakehouse-databricks"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "standard"
}
