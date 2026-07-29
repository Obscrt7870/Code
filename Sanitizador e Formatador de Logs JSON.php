<?php

class JsonLogger
{
    private string $logFile;

    public function __construct(string $logFile)
    {
        $this->logFile = $logFile;
    }

    public function log(string $level, string $message, array $context = []): void
    {
        $payload = [
            'timestamp' => date('c'),
            'level'     => strtoupper($level),
            'message'   => $message,
            'context'   => $context
        ];

        $jsonLine = json_encode($payload, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . PHP_EOL;
        file_put_contents($this->logFile, $jsonLine, FILE_APPEND | LOCK_EX);
    }
}

// Exemplo de uso
$logger = new JsonLogger(__DIR__ . '/app.log');
$logger->log('info', 'Usuário autenticado com sucesso', ['user_id' => 42, 'ip' => '192.168.1.15']);
$logger->log('warning', 'Tentativa de acesso negada', ['path' => '/admin']);

echo "[+] Registros gravados no arquivo app.log\n";