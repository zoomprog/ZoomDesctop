@echo off
powershell -executionpolicy bypass -command "Get-AppxPackage *WhatsAppDesktop* | Remove-AppxPackage"