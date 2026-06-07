# FreeRadio — Complemento para o NVDA

FreeRadio é um complemento de rádio pela Internet para o leitor de ecrã NVDA. O seu principal objetivo é dar aos utilizadores acesso fácil a milhares de estações de rádio online. Toda a interface e todas as funcionalidades foram concebidas com total acessibilidade para o NVDA.

## Diretório Radio Browser

FreeRadio utiliza a base de dados aberta [Radio Browser](https://www.radio-browser.info/) para o seu catálogo de estações. O Radio Browser é um diretório gratuito gerido pela comunidade com mais de 50.000 estações de rádio online de todo o mundo. Não é necessário registo e a API é aberta a todos.

Cada estação inclui endereço, país, género, idioma e bitrate; as estações são classificadas por votos dos utilizadores. O FreeRadio liga-se à API através de servidores espelho localizados na Alemanha, Países Baixos e Áustria; se um servidor estiver inacessível, muda automaticamente para o seguinte.

## Adicionar uma Estação ao Radio Browser

Se a estação que procura não estiver no diretório Radio Browser, pode submetê-la em [https://www.radio-browser.info/add](https://www.radio-browser.info/add). Não é necessária conta nem registo.

Preencha o formulário da página:

- **URL da transmissão (Stream URL)** *(obrigatório)* — o endereço direto da transmissão de áudio, terminado em `.mp3`, `.aac`, `.ogg` ou semelhante. Não é o endereço do site da estação, mas sim o endereço bruto da transmissão que colaria num leitor multimédia. A maioria das estações publica o URL da transmissão no seu site ou na secção "Ouvir em direto".
- **Nome da estação** *(obrigatório)* — o nome da estação tal como deve aparecer no diretório.
- **Página inicial** — o endereço do site da estação.
- **País e idioma** — selecione o país de emissão e o idioma a partir das listas pendentes.
- **Etiquetas** — palavras-chave de género ou tema separadas por vírgulas, por exemplo `notícias`, `jazz`, `clássica`. São utilizadas para pesquisa e filtragem.
- **URL do logótipo** — uma ligação direta à imagem do logótipo da estação, se disponível.

Após a submissão, a estação é revista e adicionada ao diretório público. Uma vez aceite, aparecerá automaticamente nas pesquisas e nas listagens por país do FreeRadio, uma vez que o diretório é atualizado a partir da API em tempo real.

## Requisitos

- NVDA 2024.1 ou posterior
- Windows 10 ou posterior
- Ligação à Internet

## Instalação

Descarregue o ficheiro `.nvda-addon`, prima Enter sobre ele e reinicie o NVDA quando solicitado.

## Atalhos de Teclado

Todos os atalhos podem ser reatribuídos em Menu NVDA → Preferências → Definir comandos → FreeRadio. Estes atalhos funcionam em qualquer lugar, independentemente da janela que estiver em foco.

| Atalho | Função | Descrição |
|---|---|---|
| `Ctrl+Win+R` | Abrir navegador de estações | Abre a janela do navegador se estiver fechada, ou traz-a para primeiro plano se já estiver aberta. |
| `Ctrl+Win+P` | Pausar / retomar | Pausa a estação atual se estiver a reproduzir; retoma se estiver em pausa. Se nada estiver a reproduzir, inicia a última estação ou abre a lista de favoritos conforme a definição. Premir duas vezes rapidamente salta diretamente para um separador à escolha. Premir três vezes pode desencadear uma ação separada conforme a definição. |
| `Ctrl+Win+S` | Parar | Para completamente a estação atual e reinicia o leitor. |
| `Ctrl+Win+→` | Próximo favorito | Avança para a próxima estação na lista de favoritos. Volta ao início no final da lista. |
| `Ctrl+Win+←` | Favorito anterior | Recua para a estação anterior na lista de favoritos. Salta para o fim quando está no início. |
| `Ctrl+Win+↑` | Aumentar volume | Aumenta o volume em 10; máximo 100. |
| `Ctrl+Win+↓` | Diminuir volume | Diminui o volume em 10; mínimo 0. |
| `Ctrl+Win+V` | Adicionar aos favoritos | Adiciona a estação em reprodução à lista de favoritos. Anuncia se a estação já está na lista. |
| `Ctrl+Win+I` | Informação da estação | Anuncia o nome da estação em reprodução. Premir duas vezes mostra detalhes como país, género e bitrate numa caixa de diálogo. Premir três vezes copia as informações da faixa atual (metadados ICY) para a área de transferência, se disponíveis; se não existirem metadados, inicia o reconhecimento musical Shazam. Premir quatro vezes força o reconhecimento musical em caso de metadados ICY incorretos. |
| `Ctrl+Win+M` | Espelho de áudio | Espelha a transmissão atual para um dispositivo de saída de áudio adicional em simultâneo. Prima novamente para parar o espelhamento. |
| `Ctrl+Win+E` | Gravação instantânea | Prima uma vez para iniciar a gravação da estação atual; prima novamente para parar. Prima **duas vezes** para iniciar uma **gravação de canção** — o ficheiro recebe o nome da faixa atual e a gravação para automaticamente quando a faixa muda. Prima duas vezes novamente enquanto uma gravação de canção está ativa para terminá-la antecipadamente. A reprodução continua sem interrupção em todos os modos de gravação. Disponível apenas em estações que difundem metadados ICY. |
| `Ctrl+Win+W` | Abrir pasta de gravações | Abre a pasta com os ficheiros gravados no Explorador de Ficheiros. |
| *(não atribuído)* | Alternar silenciamento de notificações | Ativa ou desativa o silenciamento de notificações em tempo real. Pode atribuir uma combinação de teclas em Menu NVDA → Preferências → Definir comandos → FreeRadio. |

Os atalhos seguinte/anterior apenas navegam na lista de favoritos; não funcionam com a lista de todas as estações. Quando uma lista está em foco na janela do navegador, as teclas de seta esquerda e direita têm a mesma função — consulte Atalhos na Caixa de Diálogo.

## Navegador de Estações

O FreeRadio adiciona também um submenu **FreeRadio** ao menu Ferramentas do NVDA, a partir do qual pode abrir diretamente o Navegador de Estações e as Definições do FreeRadio.

A janela aberta com `Ctrl+Win+R` contém cinco separadores: Todas as Estações, Favoritos, Gravação, Temporizador e Músicas Gostadas. Pode navegar entre separadores com `Ctrl+Tab`.

Quando o separador Todas as Estações abre, as 1.000 estações mais votadas são carregadas automaticamente a partir do Radio Browser. Selecionar um país na lista pendente atualiza a lista para mostrar as estações desse país. Escrever no campo de pesquisa executa automaticamente uma pesquisa completa na base de dados Radio Browser em simultâneo por nome, país e género (com um atraso de 500 ms após a última tecla premida); não é necessário premir Enter nem qualquer botão.

A lista pendente **Dispositivo de saída** na parte inferior da janela do navegador — fora dos separadores — lista todos os dispositivos de saída de áudio reconhecidos pelo BASS. Selecionar um dispositivo redireciona imediatamente o áudio para ele e guarda a escolha permanentemente; o mesmo dispositivo é utilizado automaticamente na próxima sessão. Se o dispositivo selecionado não estiver ligado, o complemento reverte automaticamente para a predefinição do sistema. Este controlo só é funcional quando o backend BASS está ativo.

Os controlos **Volume** (0–200) e **Efeitos** na mesma área podem ser ajustados em qualquer altura com a janela aberta. Na lista de Efeitos, é possível ativar simultaneamente Chorus, Compressor, Distortion, Echo, Flanger, Gargle, Reverb, EQ: Bass Boost, EQ: Treble Boost e EQ: Vocal Boost; as alterações são aplicadas à transmissão ativa instantaneamente. Estes controlos só são totalmente funcionais quando o backend BASS está ativo.

Quando um ou mais efeitos EQ estão ativos, surge automaticamente um **controlo de ganho** para cada banda ativa. O ganho pode ser ajustado entre −15 dB e +15 dB; os valores predefinidos são Graves +9 dB, Agudos +9 dB e Vocal +6 dB. Os controlos só aparecem para as bandas EQ selecionadas e ocultam-se automaticamente quando o efeito é desmarcado. Os valores são guardados permanentemente e restaurados na sessão seguinte.

O botão **Reproduzir/Pausar** encontra-se também na parte inferior da janela. Se nenhuma estação estiver a reproduzir, inicia a estação selecionada; se uma estação já estiver em reprodução, pausa a reprodução.

Quando uma estação está selecionada na lista, o botão **Detalhes da Estação** apresenta informações como país, idioma, género, formato, bitrate, website e URL da transmissão numa caixa de diálogo separada. Cada campo aparece na sua própria caixa de texto só de leitura; pode mover-se entre campos com Tab e copiar todas as informações para a área de transferência de uma só vez com o botão **Copiar tudo para a área de transferência**. Este botão está disponível nos separadores Todas as Estações e Favoritos.

### Atalhos na Caixa de Diálogo

As teclas seguintes funcionam apenas quando a janela do Navegador de Estações está ativa.

### Teclas F

| Atalho | Função | Descrição |
|---|---|---|
| `F1` | Guia de ajuda | Abre o ficheiro de ajuda do complemento no browser predefinido. É pesquisado primeiro o guia para o idioma do NVDA ativo; se não for encontrado, abre o guia predefinido. |
| `F2` | Informação da estação | Anuncia o nome da estação em reprodução. Premir duas vezes mostra detalhes como país, género e bitrate numa caixa de diálogo. Premir três vezes copia as informações da faixa atual (metadados ICY) para a área de transferência, se disponíveis; se não existirem metadados, inicia o reconhecimento musical Shazam. Premir quatro vezes força o reconhecimento musical em caso de metadados ICY incorretos. |
| `F3` | Estação anterior | Recua para a estação anterior no separador Todas as Estações ou Favoritos e inicia a reprodução imediatamente. Salta para o fim quando está no início da lista. |
| `F4` | Próxima estação | Avança para a próxima estação no separador Todas as Estações ou Favoritos e inicia a reprodução imediatamente. Volta ao início no final da lista. |
| `F5` | Diminuir volume | Diminui o volume em 10 (mínimo 0). |
| `F6` | Aumentar volume | Aumenta o volume em 10 (máximo 200). |
| `F7` | Pausar / retomar | Pausa se uma estação estiver a reproduzir; retoma se estiver em pausa e os média estiverem carregados. |
| `F8` | Parar | Para completamente a estação atual e reinicia o leitor. |
| `F9` | Renomear | Abre a caixa de diálogo de renomeação para a estação em foco no separador Favoritos. |

### Atalhos de Lista e Navegação

| Atalho | Função | Descrição |
|---|---|---|
| `→` | Próxima estação | Quando a lista Todas as Estações ou Favoritos está em foco, avança para a próxima estação e reproduz-a imediatamente. Volta ao início no final da lista. |
| `←` | Estação anterior | Quando a lista Todas as Estações ou Favoritos está em foco, recua para a estação anterior e reproduz-a imediatamente. Salta para o fim quando está no início. |
| `Enter` | Reproduzir | Quando a lista Todas as Estações ou Favoritos está em foco, inicia a reprodução da estação selecionada imediatamente. Muda para a estação selecionada mesmo que outra estação já esteja a reproduzir. |
| `Espaço` | Reproduzir / Pausar | Pausa se uma estação estiver a reproduzir; caso contrário, inicia a reprodução da estação selecionada. |
| `Ctrl+Tab` | Próximo separador | Muda para o próximo separador (Todas as Estações → Favoritos → Gravação → Temporizador → Músicas Gostadas). |
| `Ctrl+Shift+Tab` | Separador anterior | Volta ao separador anterior. |
| `Escape` | Ocultar | Oculta a janela; o complemento continua a reproduzir em segundo plano. |

### Atalhos de Volume

| Atalho | Função | Descrição |
|---|---|---|
| `Ctrl+↑` | Aumentar volume | Aumenta o volume em 10. Só funciona com a janela do navegador aberta. |
| `Ctrl+↓` | Diminuir volume | Diminui o volume em 10. Só funciona com a janela do navegador aberta. |

### Atalhos da Tecla Alt

| Atalho | Função | Descrição |
|---|---|---|
| `Alt+R` | Ir para o campo de pesquisa | Move o foco para a caixa de texto de pesquisa. Pesquisa nome, país e género em simultâneo à medida que escreve. |
| `Alt+V` | Adicionar / remover favorito | Adiciona a estação selecionada aos favoritos; remove-a se já estiver na lista. |
| `Alt+1` | Todas as Estações | Muda para o separador Todas as Estações. |
| `Alt+2` | Favoritos | Muda para o separador Favoritos. |
| `Alt+3` | Gravação | Muda para o separador Gravação. |
| `Alt+4` | Temporizador | Muda para o separador Temporizador. |
| `Alt+5` | Músicas Gostadas | Muda para o separador Músicas Gostadas. |
| `Alt+K` | Fechar | Fecha a janela; o complemento continua a reproduzir em segundo plano. |

## Favoritos

A lista de favoritos é uma coleção pessoal de estações guardada permanentemente. Para adicionar uma estação, selecione-a na lista e prima o botão Adicionar aos Favoritos ou use o atalho `Alt+V`. O mesmo atalho remove uma estação que já esteja na lista quando está selecionada.

Os favoritos podem ser reproduzidos com `Ctrl+Win+→` e `Ctrl+Win+←`; estes atalhos funcionam mesmo quando a janela do navegador não está aberta.

Para eliminar uma estação da lista de favoritos, selecione-a e prima o botão **Eliminar Estação** ou a tecla `Delete`. Após a eliminação, o foco e a seleção movem-se automaticamente para a estação seguinte. Se a estação eliminada era a última, o foco vai para a estação anterior. Se a lista ficar vazia, o foco vai para o botão Reproduzir.

### Reordenar Favoritos

Com uma estação selecionada no separador Favoritos, prima `vírgula` para entrar no modo de mover — ouvirá um sinal sonoro. Navegue até à posição pretendida com as teclas de seta e prima `vírgula` novamente. A estação é colocada na posição escolhida e a nova ordem é guardada imediatamente. Premir `vírgula` novamente na mesma posição cancela a operação.

### Adicionar Estação Personalizada

Para adicionar uma estação que não esteja no Radio Browser, utilize o botão Adicionar Estação Personalizada. Na caixa de diálogo que aparece, introduza o nome da estação e o URL da transmissão para a adicionar diretamente aos favoritos. As estações personalizadas podem ser reproduzidas e reordenadas tal como qualquer outro favorito.

### Perfil de Áudio da Estação

O separador Favoritos inclui dois botões para gerir as definições de áudio por estação:

**Guardar Perfil de Áudio para Esta Estação** — guarda o nível de volume atual, os efeitos ativos e os valores de ganho EQ como um perfil associado a essa estação específica. Sempre que essa estação iniciar a reprodução, o volume, efeitos e ganho guardados são automaticamente aplicados, substituindo as predefinições globais.

**Limpar Perfil de Áudio** — remove o perfil de áudio guardado da estação selecionada. Após limpar, a estação reverte para as definições globais de volume, efeitos e ganho EQ. Este botão só está ativo quando a estação selecionada já tem um perfil guardado.

Ambos os botões estão localizados abaixo da lista de favoritos e só estão ativos quando uma estação da lista está selecionada.

## Reconhecimento Musical

Premir `Ctrl+Win+I` três vezes ativa o reconhecimento musical baseado em Shazam para a transmissão em reprodução. O reconhecimento só inicia quando não existem metadados ICY (informações de faixa difundidas pela estação) disponíveis; se existirem metadados, estes são copiados para a área de transferência.

O reconhecimento funciona da seguinte forma: uma curta amostra de áudio é capturada da transmissão usando ffmpeg, o algoritmo de identificação Shazam é aplicado e o resultado é enviado para os servidores Shazam. Se o reconhecimento for bem-sucedido, o título da faixa, artista, álbum e ano de lançamento são anunciados pelo NVDA e copiados automaticamente para a área de transferência. Se a opção **Guardar músicas gostadas em ficheiro de texto** estiver ativa, o resultado do reconhecimento é também adicionado ao ficheiro `likedSongs.txt`.

**Feedback sonoro:** Dois sinais sonoros ascendentes indicam o início do reconhecimento e dois descendentes indicam o fim. Um sinal sonoro curto soa a cada 2 segundos enquanto o processo está em execução.

**Requisito:** É necessário `ffmpeg.exe`. Um `ffmpeg.exe` colocado na pasta do complemento é utilizado automaticamente; se estiver noutro local, o caminho pode ser definido nas Definições. Descarregue o ffmpeg em [ffmpeg.org](https://ffmpeg.org/download.html).

## Espelho de Áudio

O atalho `Ctrl+Win+M` duplica a transmissão atual para um segundo dispositivo de saída de áudio em simultâneo.

Na primeira pressão, aparece uma caixa de diálogo de seleção com os dispositivos de saída disponíveis. Depois de escolher um dispositivo, o espelhamento inicia e a reprodução principal continua sem interrupção. Prima o atalho novamente para parar o espelhamento.

**Casos de utilização:**
- **Colunas + auscultadores** — Permita que um convidado acompanhe a mesma transmissão nos auscultadores enquanto ouve pelas colunas do computador.
- **Configuração de gravação** — Direcione a saída principal para colunas e a segunda saída para um gravador externo ou interface de áudio para captura externa.
- **Multi-divisão** — Reproduza através de um altifalante Bluetooth e do altifalante integrado em simultâneo; não é necessário software adicional para levar o áudio para outra divisão.
- **Monitorização remota** — Numa sessão de partilha de ecrã ou ambiente de trabalho remoto, tanto o lado local como o remoto podem ouvir a mesma transmissão em simultâneo.

> **Nota:** O espelho de áudio só está disponível quando o backend BASS está ativo. Se o volume for alterado enquanto o espelhamento está ativo, ambas as saídas são atualizadas em simultâneo.

## Gravação

As gravações são guardadas por predefinição em `Documents\FreeRadio Recordings\`. O nome do ficheiro inclui o nome da estação e a hora de início da gravação. A pasta de gravações pode ser alterada em qualquer altura em Menu NVDA → Preferências → Definições → FreeRadio → **Pasta de gravações**. Uma vez que o motor de gravação se liga diretamente à transmissão, o áudio é escrito em disco tal como é recebido — sem processamento nem recodificação; a qualidade da gravação é idêntica à qualidade da emissão.

**Gravação instantânea:** Enquanto uma estação está a reproduzir, prima `Ctrl+Win+E`. Prima novamente para parar. A reprodução continua sem interrupção.

**Gravação de canção:** Prima `Ctrl+Win+E` **duas vezes** rapidamente enquanto uma estação que difunde metadados ICY está a reproduzir. A gravação inicia imediatamente e recebe o nome do título da faixa atual. Quando a faixa muda, a gravação para automaticamente e o NVDA anuncia o nome do ficheiro guardado. Se pretender terminar a gravação antes de a faixa terminar, prima `Ctrl+Win+E` duas vezes novamente. Se a estação atual não difundir metadados ICY, a gravação de canção não está disponível e o NVDA irá informá-lo.

**Gravação agendada:** Abra o separador Gravação no navegador. Selecione uma estação dos seus favoritos, introduza a hora de início no formato HH:MM e a duração em minutos, depois escolha um modo de gravação:

- **Gravar enquanto ouve** — reproduz e grava em simultâneo. É iniciado um backend de reprodução seguindo a ordem de prioridade BASS → VLC → PotPlayer → Windows Media Player.
- **Apenas gravar** — grava silenciosamente em segundo plano sem qualquer saída de áudio; o motor de gravação liga-se diretamente à transmissão.

Se a hora introduzida já tiver passado, a gravação é agendada para o dia seguinte. O NVDA anuncia quando uma gravação inicia e quando termina.

## Temporizador

Abra o separador Temporizador no navegador de estações (`Alt+4`). É possível adicionar dois tipos de temporizador:

**Alarme — iniciar rádio:** Inicia automaticamente a reprodução de uma estação selecionada dos seus favoritos à hora especificada. Escolha uma estação e introduza a hora no formato HH:MM.

**Suspensão — parar rádio:** Para a reprodução à hora especificada. Quando o temporizador dispara, o volume é reduzido gradualmente durante 60 segundos antes de parar a reprodução. Não é necessário selecionar uma estação; basta introduzir a hora.

Para ambos os tipos, se a hora introduzida já tiver passado, a ação é agendada para o dia seguinte. Os temporizadores pendentes estão listados no separador; selecione um e prima o botão Remover Temporizador Selecionado para o cancelar.

## Definições

As seguintes opções podem ser configuradas em Menu NVDA → Preferências → Definições → FreeRadio:

| Opção | Descrição |
|---|---|
| Dispositivo de saída de áudio (backend BASS) | Define o dispositivo de saída de áudio para reprodução de rádio. A lista inclui todos os dispositivos compatíveis com BASS no sistema, mais uma opção "Predefinição do sistema". As alterações são aplicadas imediatamente ao guardar; se o dispositivo selecionado for desligado, o complemento reverte automaticamente para a predefinição do sistema e anuncia a alteração. Só ativo quando o backend BASS está em uso. |
| Volume | Define o volume inicial do complemento (0–200). As alterações feitas durante a reprodução com `Ctrl+Win+↑` / `Ctrl+Win+↓` também são refletidas aqui. |
| Efeito de áudio predefinido | Define o efeito de áudio aplicado quando o NVDA inicia ou uma estação começa a reproduzir. O efeito selecionado corresponde à lista de Efeitos no Navegador de Estações. Só ativo quando o backend BASS está em uso. |
| Ganho EQ (graves / agudos / vocal) | Define o nível de ganho em dB para cada banda EQ (de −15 a +15). O controlo aparece automaticamente quando o efeito EQ correspondente está ativo e oculta-se quando é desativado. Os valores são guardados globalmente; podem ser substituídos por estação através do botão **Guardar Perfil de Áudio** no separador Favoritos. Só ativo quando o backend BASS está em uso. |
| Transição entre estações (backend BASS) | Controla o comportamento de transição ao mudar de estação. **Corte imediato** (predefinição) para a estação anterior imediatamente antes de a nova começar. **Transição curta (1 segundo)** e **Transição normal (2 segundos)** iniciam a nova estação sem pausa, desvanecendo gradualmente a anterior em segundo plano assim que o novo fluxo é confirmado. Não tem efeito nem impacto no desempenho quando definido como Corte imediato. Só disponível com o backend BASS. |
| Retomar última estação ao iniciar o NVDA | Quando ativado, a última estação reproduzida reinicia automaticamente sempre que o NVDA inicia. |
| Anunciar automaticamente mudanças de faixa (metadados ICY) | Quando ativado, o NVDA lê automaticamente o novo nome da faixa sempre que muda numa estação que difunde metadados ICY. A primeira faixa também é anunciada imediatamente ao mudar para uma nova estação. Desativado por predefinição. |
| Silenciar notificações (mudanças de estação, reprodução, gravação) | Quando ativado, o NVDA deixa de anunciar mudanças de estação, alterações do estado de reprodução (reproduzir, pausar, parar) e eventos de gravação (iniciada, parada, concluída). Mensagens de erro, feedback de favoritos, resultados do reconhecimento musical e notificações de atualização não são afetados. Pode também ser alternado em tempo real através de um gesto de entrada não atribuído. Desativado por predefinição. |
| Guardar músicas gostadas em ficheiro de texto | Quando ativado, as informações de faixa copiadas para a área de transferência ao premir `Ctrl+Win+I` três vezes são também adicionadas a `Documents\FreeRadio Recordings\likedSongs.txt`. Se não existirem metadados ICY, o resultado do reconhecimento Shazam é guardado no mesmo ficheiro. Desativado por predefinição. |
| Quando Ctrl+Win+P é premido sem reprodução ativa | Determina o que acontece quando este atalho é premido e nada está a reproduzir: iniciar a última estação ou abrir a lista de favoritos. |
| Quando Ctrl+Win+P é premido duas vezes | Seleciona o que acontece quando o atalho é premido duas vezes rapidamente: não fazer nada, abrir a lista de favoritos, abrir o separador de gravação ou abrir o separador do temporizador. Quando "não fazer nada" está selecionado, a primeira pressão responde instantaneamente sem atraso. |
| Quando Ctrl+Win+P é premido três vezes | Seleciona o que acontece quando o atalho é premido três vezes rapidamente: não fazer nada, abrir a lista de favoritos, abrir o separador de pesquisa, abrir o separador de gravação ou abrir o separador do temporizador. |
| Caminho do ffmpeg.exe | Caminho para o ffmpeg.exe utilizado no reconhecimento musical. Se deixado em branco, é utilizado automaticamente um ffmpeg.exe na pasta do complemento. |
| Caminho do VLC | Se o VLC não estiver instalado ou estiver numa localização não padrão, pode ser introduzido aqui o caminho completo para o executável. |
| Caminho do wmplayer.exe | Introduza aqui o caminho para o Windows Media Player, se necessário. |
| Caminho do PotPlayer | Se o PotPlayer estiver numa localização não padrão, o seu caminho pode ser introduzido aqui. |
| Pasta de gravações | Define a pasta onde os ficheiros gravados são guardados. Se deixado em branco, é utilizada a localização predefinida `Documents\FreeRadio Recordings\`. Um botão Procurar permite selecionar a pasta de forma interativa. As alterações têm efeito imediatamente após guardar. |
| Verificar atualizações automaticamente | Quando ativado, é efetuada uma verificação de atualizações em segundo plano sempre que o NVDA inicia; é emitida uma notificação se for encontrada uma nova versão. Quando desativado, as verificações automáticas são interrompidas mas as verificações manuais continuam disponíveis. |
| Desativar verificação de conectividade à Internet antes de reproduzir | Recomendado para utilizadores que experimentam um atraso antes de uma estação começar a reproduzir. Também útil quando o DNS está bloqueado. |

## Silenciamento de Notificações

Quando a opção **Silenciar notificações** está ativada nas Definições, o NVDA suprime os seguintes anúncios automáticos:

- Nome da estação quando uma nova estação começa a reproduzir
- Alterações do estado de reprodução: reproduzir, pausar, parar
- Eventos de gravação: iniciada, parada, concluída (gravações instantâneas, de canção e agendadas)
- Anúncios de mudança de faixa, mesmo quando **Anunciar automaticamente mudanças de faixa** também está ativo

Os seguintes anúncios **não** são afetados intencionalmente: mensagens de erro, feedback de favoritos (adicionado / já na lista), resultados do reconhecimento musical e notificações de atualização.

A definição pode ser alternada em Menu NVDA → Preferências → Definições → FreeRadio, ou em tempo real através de um gesto de entrada não atribuído (atribua um em Menu NVDA → Preferências → Definir comandos → FreeRadio). Quando alternada, o NVDA anuncia uma vez "Notificações silenciadas" ou "Notificações reativadas" para confirmar a alteração.

## Anúncio Automático de Mudanças de Faixa

Quando a opção **Anunciar automaticamente mudanças de faixa** está ativada nas Definições, o FreeRadio verifica os metadados ICY da estação ativa em segundo plano aproximadamente a cada 5 segundos. Quando a faixa muda, o novo título é automaticamente lido pelo NVDA — sem necessidade de premir qualquer tecla.

Ao mudar para uma nova estação, as primeiras informações de faixa são anunciadas assim que a ligação é estabelecida. Se mudar para uma estação que não difunde metadados ICY, o sistema permanece silencioso e as informações da faixa anterior não são repetidas.

Esta funcionalidade está desativada por predefinição e pode ser ativada em Menu NVDA → Preferências → Definições → FreeRadio.

## Músicas Gostadas

Quando a opção **Guardar músicas gostadas em ficheiro de texto** está ativada, as informações de faixa copiadas para a área de transferência ao premir `Ctrl+Win+I` três vezes são também adicionadas linha a linha a `Documents\FreeRadio Recordings\likedSongs.txt`.

Nas estações que difundem metadados ICY, o título e o artista da faixa são guardados diretamente. Nas estações sem metadados ICY, o resultado do reconhecimento Shazam é guardado no mesmo ficheiro — ambas as fontes partilham a mesma lista. O ficheiro é criado automaticamente se não existir; cada entrada é adicionada ao fim do ficheiro e as entradas anteriores nunca são eliminadas.

## Separador Músicas Gostadas

O separador **Músicas Gostadas** no navegador de estações apresenta todas as faixas guardadas em `likedSongs.txt`. A lista é recarregada automaticamente do ficheiro sempre que o separador é aberto.

Selecionar uma faixa da lista ativa as seguintes ações:

- **Reproduzir no Spotify:** Tenta abrir diretamente a aplicação Spotify para computador. Se a aplicação não estiver instalada, abre o site do Spotify e inicia automaticamente a reprodução do primeiro resultado.
- **Reproduzir no YouTube (`Alt+O`):** Pesquisa a faixa selecionada no YouTube e abre os resultados no browser predefinido.
- **Remover (`Alt+M`):** Elimina a faixa selecionada de `likedSongs.txt` e atualiza a lista.
- **Atualizar (`Alt+E`):** Recarrega a lista do ficheiro.

Os botões Spotify, YouTube e Remover só estão ativos quando uma faixa real está selecionada na lista.

## Reprodução

Ordem de prioridade dos backends:

1. **BASS** — o backend principal e predefinido. Não é necessária instalação separada; está incluído no complemento. O BASS envia o áudio diretamente para a pilha de áudio do Windows e aparece no misturador de volume do Windows como uma fonte de áudio independente com o nome "pythonw.exe", separada do NVDA. Isto significa que o áudio do FreeRadio circula num canal completamente separado do sintetizador de voz do NVDA: o rádio não é interrompido, não se mistura nem é afetado pelas definições de áudio do NVDA enquanto este fala. O utilizador pode ajustar o volume do rádio independentemente do NVDA no Misturador de Volume do Windows. Suporta HTTP, HTTPS e a maioria dos formatos de transmissão incorporados. O espelho de áudio só está disponível com este backend.
2. **VLC** — assume o controlo se o BASS falhar. Pesquisado automaticamente nas localizações de instalação comuns, pastas de perfil de utilizador e no PATH do sistema.
3. **PotPlayer** — tentado se o VLC não for encontrado. Pesquisado automaticamente nas localizações de instalação comuns.
4. **Windows Media Player** — utilizado como último recurso; requer que o componente WMP esteja instalado no sistema.

## Verificação de Atualizações

O FreeRadio verifica automaticamente a existência de novas versões através do GitHub.

**Verificação automática:** É executada silenciosamente em segundo plano 15 segundos após o NVDA iniciar. Se for encontrada uma nova versão, é emitida uma notificação; se não for encontrada nenhuma, não é apresentada qualquer mensagem.

**Verificação manual:** Pode ser acionada em qualquer altura em Ferramentas NVDA → FreeRadio → **Verificar Atualizações…**. Quando iniciada desta forma, o resultado é anunciado mesmo que a versão esteja atualizada.

**Quando é encontrada uma atualização:** Abre-se uma caixa de diálogo com o número da versão e a sua versão instalada.

- Se estiver disponível um ficheiro `.nvda-addon` diretamente descarregável na versão do GitHub, é apresentado o botão **Descarregar e Instalar**. Após confirmação, o ficheiro é descarregado em segundo plano, o NVDA anuncia quando o descarregamento inicia e o ecrã de instalação do NVDA abre automaticamente.
- Se não estiver disponível uma ligação de descarregamento direto, é apresentado o botão **Abrir Página** e a página da versão do GitHub abre no browser predefinido.

**Para desativar as verificações automáticas:** Desative a opção **Verificar atualizações automaticamente** em Menu NVDA → Preferências → Definições → FreeRadio.

## Licença

GPL v2