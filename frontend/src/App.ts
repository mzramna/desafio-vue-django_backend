/* eslint-disable no-console */
import { Options, Vue } from "vue-class-component";
import axios from "axios";
import ElementoPesquisado from "./components/elementoPesquisado.vue";
import { Produto } from "./produto";

@Options({
  components: {
    elementoPesquisado: ElementoPesquisado,
  },
})
export default class App extends Vue {
  exibir = false;

  emPesquisa = false;

  produtos: Produto[] = [];

  produtoPesquisado = "";

  quantidadeProdutos = 24;

  async onSubmit(): Promise<void> {
    this.exibir = false;
    this.emPesquisa = true;
    this.produtos = await this.pesquisar();
    this.emPesquisa = false;
    this.exibir = true;
  }

  async pesquisar(): Promise<Produto[]> {
    const pesquisa = { palavrasChave: this.produtoPesquisado, quantidade: this.quantidadeProdutos };
    const api = axios.create({
      baseURL: "http://backend:8000/",
    });
    const { data, status } = await api.post<Produto[], any>("pesquisa/", pesquisa);
    return data;
  }
}
