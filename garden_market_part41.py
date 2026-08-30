# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: GardenMarket
def dry_run(self):
        """Возвращает результат операции в режиме DryRun, не меняя данные."""
        if self._mode == "dry-run":
            return {
                "status": "dry_run",
                "operation": self._last_op,
                "result": self._last_result,
            }
        return None
