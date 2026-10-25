import math
def find_dim(space:dict)->int:
    dim=0
    if space["type"]=="Box":
        dim=math.prod(space["shape"])
    else:
        dim=space["n"]
    
    return dim

def auto_mlp_from_spaces(obs_space: dict, act_space: dict, hidden_layers: list) -> dict:
    """
    Automatically determine MLP architecture from environment space definitions.

    Args:
        obs_space: dict with 'type' and type-specific keys defining the observation space
        act_space: dict with 'type' and type-specific keys defining the action space
        hidden_layers: list of ints specifying hidden layer widths

    Returns:
        dict with keys:
          'input_dim': int
          'output_dim': int
          'layer_shapes': list of ((weight_rows, weight_cols), (bias_dim,)) tuples
          'total_params': int
    """
    input_dim=find_dim(obs_space)
    output_dim=find_dim(act_space)
    dimens={"input_dim":input_dim,"output_dim":output_dim}
    if hidden_layers:
        layers=[((input_dim,hidden_layers[0]),(hidden_layers[0],))]
        parameters = (input_dim*hidden_layers[0])+hidden_layers[0]
        for i in range(1,len(hidden_layers)):
            layers.append(((hidden_layers[i-1],hidden_layers[i]),(hidden_layers[i],)))
            parameters+=((hidden_layers[i-1]*hidden_layers[i])+hidden_layers[i])
        layers.append(((hidden_layers[-1],output_dim),(output_dim,)))
        parameters+= ((hidden_layers[-1]*output_dim)+output_dim)
    else:
        layers=[((input_dim,output_dim),(output_dim,))]
        parameters = (input_dim*output_dim)+output_dim

    dimens["layer_shapes"]=layers
    dimens["total_params"]=parameters

    return dimens
