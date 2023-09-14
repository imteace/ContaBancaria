from ContaBancaria import ContaBancaria

conta1 = ContaBancaria(52365, "Iris", 1000.0, ContaBancaria.CONTA_CORRENTE, 5000.0)
conta1.extrato()

conta1.deposita(500.0)
conta1.extrato()

conta1.saca(ContaBancaria.CONTA_CORRENTE, 300.0)
conta1.extrato()

conta1.saca(ContaBancaria.CONTA_POUPANCA, 200.0)

conta1.saca(ContaBancaria.CONTA_CORRENTE, 100000.0)
