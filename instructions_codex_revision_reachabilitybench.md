# Instructions pour Codex — Révision du papier ReachabilityBench

## Objectif général

Tu dois modifier le draft LaTeX du papier **ReachabilityBench: Diagnosing LLMs on Controlled Java Method-Reachability Tasks** afin de le préparer pour les prochaines expériences et pour une soumission ICSE 2027.

Le papier est encore en cours d’écriture. Certaines expériences ne sont pas finalisées. Tu dois donc :

1. renforcer la structure scientifique du papier ;
2. recentrer la contribution sur le caractère **contrôlé et paramétrable** du benchmark ;
3. préparer les sections à accueillir les futurs résultats ;
4. ne jamais inventer de résultats ;
5. poser des questions à l’auteur lorsque des informations manquent ;
6. insérer des `TODO:` précis uniquement quand l’information n’est pas encore disponible ou n’a pas été confirmée.

Le ton attendu est celui d’un papier de recherche ICSE : clair, rigoureux, défendable face à des reviewers exigeants.

---

## Règle principale : ne pas inventer

Ne remplis aucun résultat, nombre, modèle, score, effet statistique, valeur expérimentale, URL d’artefact ou détail matériel sans confirmation explicite de l’auteur.

Quand une information manque, tu dois d’abord poser une question.

Si l’auteur ne peut pas répondre maintenant, ajoute un `TODO:` clair et localisé dans le papier.

Exemple :

```latex
TODO: Insert final paired degradation results after the frozen rerun.
```

Évite les TODO vagues comme :

```latex
TODO: improve this.
```

Préférer :

```latex
TODO: Report whether the unguarded and condition-aware datasets are paired instance-by-instance, and adapt the statistical test accordingly.
```


---

## Source de vérité technique : script de génération du dataset

Avant de poser certaines questions à l’auteur ou d’insérer un `TODO:`, tu dois essayer de répondre aux questions techniques en consultant le script de génération utilisé pour produire les datasets :

```text
/home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/code_generation/multi_language_experiment_generator.py
```

Ce script doit être traité comme une source de vérité technique pour les éléments liés à la génération, par exemple :

- structure des graphes générés ;
- valeur effective de `p` si elle est codée dans le générateur ;
- paramètres de contexte ;
- nombre de méthodes ;
- génération des `if` et des conditions ;
- distinction entre appels syntaxiques et appels exécutables ;
- format des fichiers produits ;
- calcul des traces oracle ;
- calcul ou stockage des distances signées ;
- sampling des questions positives/négatives ;
- éventuelle présence de variables, paramètres, boucles et commentaires.

Procédure attendue :

1. Inspecte d’abord ce script pour les questions qui peuvent être résolues directement par le code.
2. Si le script donne une réponse claire, utilise cette information dans le papier et ajoute une formulation prudente si nécessaire.
3. Si le script est ambigu, contradictoire avec le draft, ou dépend d’arguments externes/configurations non visibles, pose une question à l’auteur.
4. Si l’information ne peut pas être confirmée, insère un `TODO:` localisé et précis.
5. N’invente jamais un comportement du générateur à partir du nom d’une variable : vérifie la logique effective du code.
6. Si tu modifies le papier à partir du script, ajoute une note interne dans ton résumé de modification indiquant quelles informations viennent du script et quelles informations restent à confirmer par l’auteur.

Exemple de comportement attendu :

- Si le script montre que `p = 0.65` est codé par défaut mais peut être modifié par argument CLI, écrire dans le papier que la valeur finale doit être confirmée pour les datasets gelés.
- Si le script montre que la trace canonique est produite par une fonction précise, aligner la définition du papier sur cette fonction.
- Si le script ne permet pas de savoir quels arguments exacts ont été utilisés pour générer le dataset final, demander à l’auteur le fichier de configuration ou la commande de génération.

---

## Ce que le papier doit maintenant vendre

Le papier ne doit pas être présenté comme seulement :

> “We introduce a Java reachability benchmark.”

Il doit être présenté comme :

> “We introduce a controlled and parameterized Java benchmark for diagnosing which code factors make executable inter-method reachability difficult for LLMs.”

La différence essentielle est la **paramétrisation** : le benchmark permet de contrôler et mesurer l’impact de facteurs comme :

- distance canonique d’exécution ;
- nombre de méthodes dans la classe ;
- taille du contexte ;
- nombre et placement des `if` dans le condition-aware reachability ;
- polarité positive/négative ;
- divergence entre appels visibles syntaxiquement et appels réellement exécutables.

Les expériences préliminaires suggèrent déjà que :

- la distance influence les résultats ;
- le nombre de méthodes dans la classe influence les résultats ;
- dans condition-aware reachability, le nombre de `if` influence les résultats.

Ces résultats restent préliminaires. Tu dois préparer le papier pour les accueillir proprement sans les présenter comme définitifs.

---

## Questions à poser à l’auteur avant modification finale

Avant de remplacer les TODOs, tu dois demander à l’auteur les informations suivantes.

### A. Dataset et génération

1. Les datasets unguarded et condition-aware sont-ils appariés instance par instance ? Non
2. Les mêmes graphes abstraits sont-ils utilisés dans les deux familles ? Non
3. Les mêmes paires source-target sont-elles conservées entre unguarded et condition-aware ? Non
4. Quelle est la valeur finale de `nb_questions_per_depth` ? à déterminer selon les paramètres choisit pour la génération du dataset
5. Le dataset final contient-il exactement les context sizes 100, 250 et 500 ? Oui je pense
6. Les distances finales sont-elles bien 1 à 25 ? Oui je pense
7. Combien d’instances finales par famille ? à déterminer selon les paramètres choisit pour la génération du dataset
8. Combien de classes finales par famille ? ce n'est pas important
9. Le dataset est-il équilibré en positif/négatif ? Oui
10. La valeur `p = 0.65` est-elle bien fixée dans tous les datasets finaux ? Oui
11. Existe-t-il une preuve de calibration justifiant `p = 0.65` ? Oui mais juste évoquer qu'on a fait une étude sur l'influence du paramètre p sur le nombre de questions possible par code généré (surtout par rapport à la profondeur/distance car p défini quelque part la hauteur de l'arbre et le branchement, donc la profondeur/distance des questions possibles)
12. Le nombre de `if` est-il un facteur explicitement contrôlé ou seulement une propriété dérivée ? Oui c'est une propriété controlée (voir le code)
13. Les `if` sont-ils placés de façon contrôlée par rapport à la source, à la cible ou aux branches non atteignables ? voir le code 
14. Les conditions peuvent-elles dépendre de variables locales, de paramètres, ou des deux ? les deux (voir le code)
15. Les boucles existent-elles vraiment dans les instances finales ? Si oui, modifient-elles la reachability ou sont-elles uniquement du bruit de surface ? Oui elle existe, non c'est juste du bruit, il n'y a aucun appel de méthode dedans (voir le code)

### B. Trace canonique et métriques

1. Quelle est exactement la convention de parcours canonique : DFS preorder, exploration en ordre textuel, ou autre ? le parcours se fait dans l'ordre d'execution (similaire à un dfs de gauche à droite dans le graphe)
2. Le code de l’évaluateur correspond-il exactement à la définition donnée dans le papier ? (voir le code)
3. La distance signée stockée dans `reachability_questions.txt` correspond-elle bien à la distance dans la trace canonique ? oui (voir le code)
4. Comment `trace completeness` est-elle calculée : prefix overlap, ordered recall, LCS, ou autre ? (voir le code : /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/analysis/evaluate_results.py)
5. Quelle est la règle exacte pour `graph-valid exploration` dans les cas négatifs ? (voir le code : /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/analysis/evaluate_results.py et /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/analysis/deeper_analysis)
6. Une trace vide peut-elle être valide ? Non (voir le code : /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/analysis/evaluate_results.py et /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/analysis/deeper_analysis)
7. Comment sont traitées les méthodes répétées ? (voir le code : /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/analysis/evaluate_results.py et /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/analysis/deeper_analysis)
8. Comment sont traitées les méthodes inexistantes ? (voir le code : /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/analysis/evaluate_results.py et /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/analysis/deeper_analysis)
9. Comment sont traitées les sorties JSON avec plusieurs objets ? (voir le code : /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/analysis/evaluate_results.py et /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/analysis/deeper_analysis)
10. Comment sont traitées les sorties avec prose + JSON ? (voir le code : /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/analysis/evaluate_results.py et /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/analysis/deeper_analysis)
11. Les résultats stricts comptent-ils toujours `NO_RESPONSE` comme incorrect ? Oui (voir le code : /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/analysis/evaluate_results.py et /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/analysis/deeper_analysis)
12. Des scores conditionnels excluant `NO_RESPONSE` seront-ils en appendix ? Non

### D. Modèles et inférence

1. Quels modèles seront définitivement évalués ? Ceux dans le papier mais à déterminé 
2. Quels sont les identifiants exacts des checkpoints ? Ceux dans le papier mais à déterminé 
3. Quelle version du moteur d’inférence est utilisée ? vllm 0.22.0
4. Les modèles sont-ils servis avec vLLM, Transformers, SGLang, llama.cpp, ou autre ? vllm 0.22.0
5. Température finale ? température recommandée par le constructeur de modèle 
6. Top-p final ? Top-p recommandée par le constructeur de modèle 
7. Seed policy ? Non
8. Max input tokens ? Context window du modèle
9. Max output tokens ? 16384 token pour le reasoning et 2048 pour la réponse finale pour les modèles reasoning, sinon 18426 tokens (la somme des deux budget) pour le modèle non reasoning
10. Timeout par instance ? On s'en fiche
11. Retry policy ?  On s'en fiche
12. Quantization ou full precision ? fp8
13. Nombre de GPU ? 1 par modèle
14. Type de GPU sur Jean Zay ? H100 80GB sur Jean Zay IDRIS
15. Partition Jean Zay utilisée ? On s'en fiche
16. Tensor parallelism ? Non Mais on s'en fiche
17. Quels modèles supportent réellement un reasoning budget ? A voir selon les modèles
18. Le budget contrôle-t-il des tokens internes, des tokens visibles, ou seulement un paramètre du serveur ? tokens internes controllé par vllm et ses paramètres

### E. Résultats et statistiques

1. Quelles métriques seront dans le tableau principal ? Conseille moi
2. Quelles métriques iront en appendix ? Conseille moi
3. Les résultats finaux auront-ils des intervalles de confiance à 95 % ? Conseille moi
4. Quel test sera utilisé pour comparer unguarded vs condition-aware ? Conseille moi

6. Une régression logistique mixte sera-t-elle utilisée ? Conseille moi
7. Quels effets fixes seront inclus ? Conseille moi
8. Y aura-t-il un random intercept par classe générée ? On s'en fiche
9. Les interactions seront-elles testées : distance × taille de classe, famille × distance, `if` × polarité ? On s'en fiche
10. Les comparaisons multiples seront-elles corrigées ? On s'en fiche
11. Quels plots doivent être produits ? Conseille moi
12. Les résultats préliminaires doivent-ils être mentionnés dans un draft interne seulement ou jamais dans le papier soumis ? un draft interne seulement

### F. Artefact

1. L’artefact anonymisé sera-t-il disponible pour la review ? Oui
2. Où sera-t-il hébergé ? Github
3. Les raw outputs des modèles peuvent-ils être partagés ? Oui 
4. Les licences des modèles autorisent-elles le partage des sorties ? A vérifier selon les modèles
5. L’artefact contiendra-t-il les datasets générés ? Oui 
6. L’artefact contiendra-t-il le générateur ? Oui 
7. L’artefact contiendra-t-il les scripts d’inférence ? Oui 
8. L’artefact contiendra-t-il le parser ? Oui
9. L’artefact contiendra-t-il l’évaluateur ? Oui 
10. L’artefact contiendra-t-il les scripts statistiques ? Oui 
11. Un DOI ou Zenodo release est-il prévu après acceptation ? Je sais pas 

---

## Révision de la structure argumentative

### Nouvelle thèse centrale

La thèse centrale doit être :

```text
ReachabilityBench is a controlled and parameterized benchmark for diagnosing how code-structural and execution-semantic factors affect LLMs' ability to track executable inter-method reachability in Java.
```

Cette thèse doit apparaître :

- dans l’abstract ;
- dans le dernier paragraphe de l’introduction ;
- dans les contributions ;
- dans les RQs ;
- dans la discussion.

---

## Réécriture proposée de l’abstract

Ne pas remplir les valeurs `TODO` sans confirmation.

```latex
Abstract—Large language models are increasingly evaluated on realistic software-engineering tasks, but end-to-end benchmarks often conflate multiple capabilities and make it difficult to identify which code properties cause reasoning failures. We introduce ReachabilityBench, a controlled and parameterized Java benchmark for diagnosing LLMs on executable inter-method reachability. ReachabilityBench generates single-class Java programs with exact oracle labels and execution-oriented traces, and varies structural and execution-related factors such as canonical distance, class size, positive/negative polarity, and condition-aware guards. The benchmark evaluates two paired task families: unguarded reachability, where visible calls are executable, and condition-aware reachability, where syntactically visible calls may be non-executable under generated conditions. We separate final-answer correctness from exact trace accuracy, trace completeness, graph-valid exploration, syntactic-call bias, and invalid-output behavior. We evaluate TODO: insert final number of locally served LLMs on TODO: insert final number of generated instances under a fixed prompt and inference protocol. TODO: Insert final empirical takeaway about the effects of distance, class size, and condition-aware guards. ReachabilityBench complements realistic software-engineering benchmarks by isolating the factors that make executable reachability difficult under exact oracle supervision. TODO: Insert anonymized artifact statement.
```

---

## Contributions à reformuler

Remplacer les contributions actuelles par une version plus centrée sur la paramétrisation.

```latex
This paper makes the following contributions:

\begin{itemize}
    \item \textbf{A parameterized diagnostic benchmark.}
    We introduce ReachabilityBench, a controlled Java benchmark for executable inter-method reachability. Unlike broad end-to-end benchmarks, ReachabilityBench is designed to vary code factors such as canonical execution distance, class size, polarity, and condition-aware guards under exact oracle supervision.

    \item \textbf{A paired unguarded and condition-aware design.}
    ReachabilityBench separates syntactic call presence from executable reachability by comparing unguarded instances, where visible generated calls are executable, with condition-aware instances, where calls inside false branches are visible but non-executable.

    \item \textbf{Trace-aware and graph-aware evaluation.}
    We define metrics that separate final-answer correctness from exact canonical trace accuracy, trace completeness, graph-valid exploration, syntactic-call bias, and invalid-output behavior.

    \item \textbf{A controlled empirical study of LLM execution tracking.}
    We evaluate TODO: insert final model count locally served LLMs and analyze how distance, class size, condition-aware guards, and output validity affect model performance. TODO: Insert final one-sentence empirical takeaway after reruns.
\end{itemize}
```

---

## Révision des Research Questions

Remplacer les RQs actuelles par une version plus directe.

```latex
\textbf{RQ1: Can LLMs answer executable method-reachability queries and produce faithful traces?}

We measure final-answer accuracy, exact canonical trace accuracy, trace completeness, graph-valid exploration, and NO_RESPONSE.

\textbf{RQ2: Which structural factors make execution tracking harder?}

We analyze the effect of canonical execution distance, class size, polarity, and their interactions on final-answer and trace-level metrics.

\textbf{RQ3: Do condition-aware guards expose syntactic-call bias?}

We compare unguarded and condition-aware reachability, and analyze whether models incorrectly follow syntactically visible but non-executable calls. We further study how the number and placement of generated if guards affect performance.

\textbf{RQ4: Does requested reasoning budget improve reachability reasoning or mainly affect output validity?}

This RQ is secondary and applies only to models and serving configurations with verified reasoning-budget controls.
```

---

## Baselines : clarification importante

Les LLMs testés ne doivent pas être appelés les “baselines” principales.

Ils sont les **systems under evaluation** ou les **evaluated models**.

Une baseline sert à fournir un point de référence simple permettant d’interpréter les résultats. Les modèles peuvent être comparés entre eux, et un modèle plus ancien ou plus petit peut être utilisé comme **LLM baseline**, mais cela ne remplace pas des baselines non-LLM simples.

À ajouter dans la méthodologie :

```latex
\subsection{Baselines and Sanity Checks}

The evaluated LLMs are the primary systems under test rather than baselines in the classical sense. To calibrate task difficulty and interpret model failures, we include simple non-LLM baselines and oracle sanity checks.

\begin{itemize}
    \item \textbf{Random-label baseline.}
    This baseline predicts a reachability label according to the empirical label distribution and emits an empty or minimal trace. It calibrates final-answer accuracy under label balance.

    \item \textbf{Syntactic-call baseline.}
    This baseline treats every syntactically visible method call as executable. It is expected to perform well on unguarded instances but to fail on condition-aware instances when false-branch calls are visible but non-executable. This baseline directly calibrates syntactic-call bias.

    \item \textbf{Shortest-executable-path baseline.}
    Given the executable call graph, this baseline emits the shortest path from source to target for positive queries and a reachability label for negative queries. It helps separate semantic reachability from the benchmark's stricter canonical exploration convention.

    \item \textbf{Oracle-traversal baseline.}
    This deterministic baseline runs the same canonical traversal used by the oracle over the validated executable call graph. It should achieve perfect scores and serves as an implementation sanity check rather than a competing method.
\end{itemize}

TODO: Confirm which baselines are implemented in the final artifact.
```

Si toutes les baselines ne sont pas implémentées, garder seulement celles disponibles et ajouter des TODO pour les autres.

---

## Section à ajouter : pourquoi la trace canonique n’est pas injuste

Ajouter une clarification forte.

```latex
\subsection{Why Evaluate Canonical Traces?}

The canonical trace is intentionally stricter than a reachability path. A shortest path can show that the target is reachable, but it does not test whether the model follows the requested execution-oriented exploration convention. ReachabilityBench therefore reports multiple trace-level metrics. Exact canonical trace accuracy measures strict agreement with the benchmark oracle. Trace completeness captures partial recovery of the oracle exploration. Graph-valid exploration measures whether the predicted transitions are executable even when the exact canonical order is not recovered. This separation prevents the benchmark from relying on a single overly strict metric and allows us to distinguish semantic reachability, valid exploration, and exact oracle-trace following.

TODO: Ensure that the prompt, evaluator, and metric definitions consistently distinguish path validity, graph-valid exploration, and exact canonical trace equality.
```

---

## Related Work : angle à renforcer

Dans la section Related Work, renforcer la différence avec TraceEval, CORE/CoRe, REval, CRUXEval et RE2-Bench.

### Message à faire passer

- TraceEval est plus réaliste mais moins paramétrable.
- CORE/CoRe est plus large mais moins centré sur une tâche isolée de reachability exécutable.
- REval/CRUXEval évaluent le comportement d’exécution mais pas l’isolation factorielle d’un reachability inter-méthodes Java.
- RE2-Bench est une menace de validité externe : les programmes synthétiques sont moins réalistes, mais c’est le prix du contrôle.

Ajouter ou renforcer ce passage :

```latex
ReachabilityBench differs from these benchmarks less by the surface task alone than by its experimental control. Its goal is not to maximize ecological realism, but to isolate how specific code factors affect LLM execution tracking. In particular, ReachabilityBench varies canonical distance, class size, query polarity, and condition-aware guards while preserving exact oracle labels and traces. This factor-level control is difficult to obtain from real-world benchmark suites, where task difficulty, program structure, naming conventions, project architecture, and test behavior are naturally entangled.
```

---

## Methodology : modifications à faire

### Ajouter une section “Experimental Factors”

Créer une sous-section claire.

```latex
\subsection{Experimental Factors}

ReachabilityBench is parameterized along several dimensions. The final empirical study focuses on the following primary factors:

\begin{itemize}
    \item \textbf{Canonical execution distance:} the number of canonical exploration steps required to reach the target for positive queries, or to exhaust the reachable region for negative queries.
    \item \textbf{Class size:} the number of generated methods in the Java class, operationalized through context sizes TODO: confirm final values.
    \item \textbf{Query polarity:} whether the target is reachable or unreachable from the source.
    \item \textbf{Condition-aware guards:} the number and placement of generated if statements that may contain visible but non-executable calls.
\end{itemize}

Other configurable surface factors, such as comments, local variables, parameters, loops, and method declaration order, are recorded as metadata and used for secondary analyses when supported by the final dataset.

TODO: Confirm which factors are primary, which are secondary, and which are fixed in the final experiments.
```

---

## Results : structure à préparer

La section résultats doit être organisée autour des RQs.

### RQ1

Inclure :

- table principale par modèle et famille ;
- final-answer accuracy ;
- trace exact accuracy ;
- trace completeness ;
- graph-valid exploration ;
- NO_RESPONSE.

### RQ2

Inclure :

- performance vs distance ;
- performance vs class size ;
- positive vs negative ;
- interaction distance × class size ;
- final-answer vs trace metrics.

### RQ3

Inclure :

- unguarded vs condition-aware ;
- effet du nombre de `if` ;
- syntactic-call bias ;
- exemples d’erreurs.

### RQ4

Inclure seulement si les contrôles de budget sont vérifiés.

---

## Figures à prévoir

Ajouter des placeholders de figures si les résultats ne sont pas encore disponibles.

```latex
\begin{figure}
    \centering
    TODO: Insert plot of final-answer and trace accuracy by canonical distance.
    \caption{Effect of canonical execution distance on reachability performance.}
    \label{fig:distance-effect}
\end{figure}
```

```latex
\begin{figure}
    \centering
    TODO: Insert plot of final-answer and trace accuracy by class size.
    \caption{Effect of generated class size on reachability performance.}
    \label{fig:class-size-effect}
\end{figure}
```

```latex
\begin{figure}
    \centering
    TODO: Insert plot of syntactic-call bias by number of condition-aware guards.
    \caption{Effect of condition-aware guards on syntactic-call bias.}
    \label{fig:if-effect}
\end{figure}
```

---

## Error Analysis : renforcer les familles d’erreurs

Conserver la taxonomie existante, mais s’assurer que chaque famille a :

- une définition ;
- une méthode de détection ;
- un count ;
- un pourcentage ;
- au moins un exemple si c’est une erreur importante.

Familles prioritaires :

1. syntactic-call bias ;
2. missing intermediate nodes ;
3. early stopping ;
4. invalid transition ;
5. positive shortcut ;
6. negative over-exploration ;
7. wrong source ;
8. invalid JSON / schema failure.

Ajouter un passage :

```latex
The error analysis is not intended to replace the quantitative metrics. Instead, it explains the mechanisms behind aggregate degradation. In particular, syntactic-call bias tests whether condition-aware failures arise from treating visible calls as executable, while missing-node and shortcut errors test whether models answer correctly without recovering the required execution-oriented trace.
```

---

## Threats to Validity : renforcer la défense

### Construct validity

Clarifier que :

- la trace est une sortie observable ;
- elle ne prouve pas le raisonnement interne ;
- les métriques multiples évitent de surinterpréter l’exact match.

### Internal validity

Mentionner :

- erreurs du générateur ;
- mismatch entre oracle et evaluator ;
- prompt ambiguity ;
- parser failure ;
- serving configuration ;
- model version drift.

### External validity

Dire explicitement :

```latex
ReachabilityBench is not designed to represent full Java software. It intentionally omits inheritance, dynamic dispatch, exceptions, recursion, external libraries, and multi-class projects to isolate executable method-reachability under exact factor control.
```

Puis ajouter :

```latex
This limitation is also the source of the benchmark's diagnostic value: by reducing ecological realism, ReachabilityBench can vary individual factors and attribute performance degradation to controlled code properties.
```

### Conclusion validity

Mentionner :

- nécessité des reruns finaux ;
- intervalles de confiance ;
- différence entre résultats stricts et conditionnels ;
- budget sensitivity secondaire.

---

## Data Availability / Artifact

Garder la section, mais la rendre plus concrète.

```latex
The anonymized review artifact will include TODO: confirm available contents. At minimum, we plan to include the generated benchmark instances, generator configuration, oracle validators, prompt templates, parsing and evaluation scripts, statistical-analysis scripts, and documentation needed to reproduce the main tables and figures. TODO: Specify whether raw model outputs can be shared under model-license and storage constraints.
```

Après acceptation :

```latex
Upon acceptance, we plan to release the artifact through a public repository and an archival DOI-backed release.
```

---

## Terminologie à harmoniser

Utiliser systématiquement :

- `executable method reachability`
- `condition-aware reachability`
- `unguarded reachability`
- `syntactic call graph`
- `executable call graph`
- `canonical execution-oriented trace`
- `graph-valid exploration`
- `syntactic-call bias`
- `systems under evaluation`
- `non-LLM baselines`
- `oracle sanity check`

Éviter :

- “toy benchmark”
- “simple benchmark”
- “first benchmark” sans preuve
- “reasoning ability” de façon trop générale
- “baseline LLMs” pour désigner tous les modèles testés

---

## Instructions concrètes de modification du LaTeX

1. Modifier l’abstract selon la nouvelle thèse.
2. Réécrire le dernier paragraphe de l’introduction pour insister sur la paramétrisation.
3. Reformuler les contributions.
4. Renforcer Related Work avec l’angle “realistic but entangled” vs “controlled and parameterized”.
5. Ajouter une sous-section “Experimental Factors”.
6. Ajouter une sous-section “Baselines and Sanity Checks”.
7. Ajouter une sous-section “Why Evaluate Canonical Traces?”.
8. Réorganiser les RQs.
9. Clarifier les définitions de métriques.
10. Ajouter placeholders de figures pour distance, class size, number of if.
11. Renforcer threats to validity.
12. Vérifier que tous les TODOs sont précis.
13. Supprimer les répétitions défensives du type “not a replacement” quand elles apparaissent trop souvent.
14. Ne pas modifier les claims de résultats tant que les résultats finaux ne sont pas fournis.
15. Préserver l’anonymat de soumission.
16. Éviter les répétitions et les redondance et voir si le fil directeur du papier est clair et naturel.

---

## Format attendu des questions à poser à l’auteur

Quand tu as besoin d’une information, demande-la sous forme de liste courte.

Exemple :

```text
J’ai besoin de confirmer 5 points avant de remplacer les TODOs de la section Dataset:

1. Les datasets unguarded et condition-aware sont-ils appariés instance par instance ?
2. Quelle est la valeur finale de nb_questions_per_depth ?
3. Combien d’instances finales par famille ?
4. Les context sizes sont-ils bien 100, 250 et 500 ?
5. Le nombre de if est-il contrôlé explicitement ou seulement enregistré comme metadata ?

Si une information n’est pas encore fixée, je laisserai un TODO précis dans le papier.
```

---

## Politique de TODO

Utiliser trois types de TODO :

### TODO résultat

```latex
TODO: Insert final strict scores after the frozen rerun.
```

### TODO confirmation

```latex
TODO: Confirm whether the final unguarded and condition-aware datasets are paired instance-by-instance.
```

### TODO implémentation

```latex
TODO: Insert pseudocode matching the final evaluator implementation exactly.
```

Ne pas laisser de TODO générique.

---

## Résultat attendu

À la fin, le papier doit être prêt à recevoir les résultats finaux. Même sans résultats définitifs, il doit déjà montrer clairement :

1. quelle est la contribution ;
2. pourquoi elle est différente des travaux proches ;
3. quels facteurs seront étudiés ;
4. quelles métriques seront utilisées ;
5. quelles baselines seront ajoutées ;
6. quels éléments restent à confirmer ;
7. comment les prochaines expériences s’inséreront dans la narration scientifique.

Le papier final doit donner l’impression d’une étude contrôlée et rigoureuse, pas d’un simple générateur de benchmarks.