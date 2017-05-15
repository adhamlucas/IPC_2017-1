#include <bits/stdc++.h>

using namespace std;

struct Questao {
    int lista_id, questao_id;
    double dificuldade;
    Questao(int lista_id, int questao_id, double dificuldade) :
        lista_id(lista_id), questao_id(questao_id), dificuldade(dificuldade)
    {}
    void mostraInfo() {
        string lista = to_string(this->lista_id);
        string questao = to_string(this->questao_id);
        cout << "Lista " << lista << ", questão " << questao << endl;
    }
};

bool questaoPorLista(Questao& a, Questao& b) {
    if (a.lista_id < b.lista_id) {
        return true;
    } else if (a.lista_id == b.lista_id) {
        return a.questao_id < b.questao_id;
    } else {
        return false;
    }
}

struct Grupo {
    int grupo_id;
    vector <Questao> questoes;
    Grupo(int grupo_id) : grupo_id(grupo_id) {}
    void adicionaQuestao(Questao nova_questao) {
        this->questoes.emplace_back(nova_questao);
    }
    double dificuldadeTotal() {
        double dificuldade_total = 0.0;
        for (auto questao : questoes) {
            dificuldade_total += questao.dificuldade;
        }
        return dificuldade_total;
    }
    void mostraInfo() {
        sort(this->questoes.begin(), this->questoes.end(), questaoPorLista);
        cout << "Grupo " << this->grupo_id << ":\n";
        for (auto questao : this->questoes) {
            questao.mostraInfo();
        }
    }
};

bool questaoPorDificuldade(Questao& a, Questao& b) {
    return a.dificuldade > b.dificuldade;
}

bool grupoPorId(Grupo& a, Grupo& b) {
    return a.grupo_id < b.grupo_id;
}

int indiceMenorDificuldade(vector <Grupo>& grupos) {
    int menor_dificuldade_total = (int)1e9;
    int indice = -1;
    for (int i = 0; i < (int)grupos.size(); i++) {
        if (grupos[i].dificuldadeTotal() < menor_dificuldade_total) {
            menor_dificuldade_total = grupos[i].dificuldadeTotal();
            indice = i;
        }
    }
    return indice;
}

int main() {
    int qtd_lista;
    cin >> qtd_lista;
    vector <Questao> questoes;
    for (int lista_id = 1; lista_id <= qtd_lista; lista_id++) {
        int qtd_questao;
        cin >> qtd_questao;
        for (int j = 1; j <= qtd_questao; j++) {
            int questao_id;
            cin >> questao_id;
            double dificuldade = 0.0;
            // Gambiarra:
            if (j != questao_id) {
                dificuldade = 10.0;
            } else {
                dificuldade = (1.0*questao_id/qtd_questao)*5;
            }
            questoes.emplace_back(lista_id, questao_id, dificuldade);
        }
    }
    sort(questoes.begin(), questoes.end(), questaoPorDificuldade);

    int qtd_grupo;
    cin >> qtd_grupo;
    vector <Grupo> grupos;
    for (int grupo_id = 1; grupo_id <= qtd_grupo; grupo_id++) {
        grupos.emplace_back(Grupo(grupo_id));
    }
    random_shuffle(grupos.begin(), grupos.end());
    for (auto questao : questoes) {
        int i = indiceMenorDificuldade(grupos);
        grupos[i].adicionaQuestao(questao);
    }

    sort(grupos.begin(), grupos.end(), grupoPorId);

    for (auto grupo : grupos) {
        grupo.mostraInfo();
        cout << endl;
    }

    return 0;
}
