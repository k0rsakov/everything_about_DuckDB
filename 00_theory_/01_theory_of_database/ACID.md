# ACID

<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f093fb;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#f5576c;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="grad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4facfe;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#00f2fe;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="grad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#43e97b;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#38f9d7;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Background -->
  <rect width="800" height="600" fill="#1a1a2e"/>
  
  <!-- Title -->
  <text x="400" y="50" font-family="Arial, sans-serif" font-size="36" font-weight="bold" fill="#ffffff" text-anchor="middle">
    Принципы ACID
  </text>
  
  <!-- Subtitle -->
  <text x="400" y="80" font-family="Arial, sans-serif" font-size="16" fill="#a0a0a0" text-anchor="middle">
    Основа надежности транзакций в базах данных
  </text>
  
  <!-- Atomicity Block -->
  <g>
    <rect x="50" y="120" width="330" height="200" rx="15" fill="url(#grad1)" opacity="0.9"/>
    <text x="215" y="155" font-family="Arial, sans-serif" font-size="24" font-weight="bold" fill="#ffffff" text-anchor="middle">
      A - Atomicity
    </text>
    <text x="215" y="185" font-family="Arial, sans-serif" font-size="18" fill="#ffffff" text-anchor="middle">
      Атомарность
    </text>
    <text x="215" y="220" font-family="Arial, sans-serif" font-size="14" fill="#e0e0e0" text-anchor="middle">
      Транзакция выполняется полностью
    </text>
    <text x="215" y="240" font-family="Arial, sans-serif" font-size="14" fill="#e0e0e0" text-anchor="middle">
      или не выполняется вообще.
    </text>
    <text x="215" y="260" font-family="Arial, sans-serif" font-size="14" fill="#e0e0e0" text-anchor="middle">
      Принцип "всё или ничего"
    </text>
    
    <!-- Icon -->
    <circle cx="215" cy="290" r="15" fill="#ffffff" opacity="0.3"/>
    <path d="M 205 290 L 212 297 L 225 284" stroke="#ffffff" stroke-width="3" fill="none" stroke-linecap="round"/>
  </g>
  
  <!-- Consistency Block -->
  <g>
    <rect x="420" y="120" width="330" height="200" rx="15" fill="url(#grad2)" opacity="0.9"/>
    <text x="585" y="155" font-family="Arial, sans-serif" font-size="24" font-weight="bold" fill="#ffffff" text-anchor="middle">
      C - Consistency
    </text>
    <text x="585" y="185" font-family="Arial, sans-serif" font-size="18" fill="#ffffff" text-anchor="middle">
      Согласованность
    </text>
    <text x="585" y="220" font-family="Arial, sans-serif" font-size="14" fill="#e0e0e0" text-anchor="middle">
      База данных переходит из одного
    </text>
    <text x="585" y="240" font-family="Arial, sans-serif" font-size="14" fill="#e0e0e0" text-anchor="middle">
      согласованного состояния в другое.
    </text>
    <text x="585" y="260" font-family="Arial, sans-serif" font-size="14" fill="#e0e0e0" text-anchor="middle">
      Соблюдение всех правил и ограничений
    </text>
    
    <!-- Icon -->
    <circle cx="570" cy="290" r="12" fill="#ffffff" opacity="0.3"/>
    <circle cx="600" cy="290" r="12" fill="#ffffff" opacity="0.6"/>
    <path d="M 582 290 L 588 290" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
  </g>
  
  <!-- Isolation Block -->
  <g>
    <rect x="50" y="350" width="330" height="200" rx="15" fill="url(#grad3)" opacity="0.9"/>
    <text x="215" y="385" font-family="Arial, sans-serif" font-size="24" font-weight="bold" fill="#ffffff" text-anchor="middle">
      I - Isolation
    </text>
    <text x="215" y="415" font-family="Arial, sans-serif" font-size="18" fill="#ffffff" text-anchor="middle">
      Изолированность
    </text>
    <text x="215" y="450" font-family="Arial, sans-serif" font-size="14" fill="#e0e0e0" text-anchor="middle">
      Параллельные транзакции
    </text>
    <text x="215" y="470" font-family="Arial, sans-serif" font-size="14" fill="#e0e0e0" text-anchor="middle">
      не влияют друг на друга.
    </text>
    <text x="215" y="490" font-family="Arial, sans-serif" font-size="14" fill="#e0e0e0" text-anchor="middle">
      Каждая транзакция изолирована
    </text>
    
    <!-- Icon -->
    <rect x="195" y="510" width="15" height="25" rx="2" fill="#ffffff" opacity="0.3"/>
    <rect x="210" y="510" width="15" height="25" rx="2" fill="#ffffff" opacity="0.6"/>
    <rect x="225" y="510" width="15" height="25" rx="2" fill="#ffffff" opacity="0.3"/>
  </g>
  
  <!-- Durability Block -->
  <g>
    <rect x="420" y="350" width="330" height="200" rx="15" fill="url(#grad4)" opacity="0.9"/>
    <text x="585" y="385" font-family="Arial, sans-serif" font-size="24" font-weight="bold" fill="#ffffff" text-anchor="middle">
      D - Durability
    </text>
    <text x="585" y="415" font-family="Arial, sans-serif" font-size="18" fill="#ffffff" text-anchor="middle">
      Долговечность
    </text>
    <text x="585" y="450" font-family="Arial, sans-serif" font-size="14" fill="#e0e0e0" text-anchor="middle">
      Результат успешной транзакции
    </text>
    <text x="585" y="470" font-family="Arial, sans-serif" font-size="14" fill="#e0e0e0" text-anchor="middle">
      сохраняется навсегда.
    </text>
    <text x="585" y="490" font-family="Arial, sans-serif" font-size="14" fill="#e0e0e0" text-anchor="middle">
      Данные не потеряются при сбоях
    </text>
    
    <!-- Icon -->
    <rect x="570" y="510" width="30" height="25" rx="3" fill="#ffffff" opacity="0.3"/>
    <circle cx="585" cy="522" r="8" fill="#ffffff" opacity="0.6"/>
    <path d="M 585 517 L 585 527 M 580 522 L 590 522" stroke="#1a1a2e" stroke-width="2"/>
  </g>
</svg>