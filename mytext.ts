import {HTMLBox, HTMLBoxView} from "models/layouts/html_box"

import {div} from "core/dom"
import * as p from "core/properties"

export class MyTextView extends HTMLBoxView {
  model: MyText

  render(): void {
    super.render()
    this.el.appendChild(div({}, this.model.text.join(' - ')))
  }
}

export namespace MyText {
  export type Attrs = p.AttrsOf<Props>
  export type Props = HTMLBox.Props & {
    text: p.Property<string[]>
  }
}

export interface MyText extends MyText.Attrs {}

export class MyText extends HTMLBox {
  properties: MyText.Props

  static init_MyText(): void {
    this.prototype.default_view = MyTextView
    this.define<MyText.Props>({
      text: [p.Array, []],
    })
  }
}
