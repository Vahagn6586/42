/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   handle_X.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/12 20:38:42 by vrafyan           #+#    #+#             */
/*   Updated: 2026/03/12 20:38:43 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	handle_x_up(va_list *arg)
{
	unsigned int	val;
	char			*ret;
	int				ret_val;

	val = va_arg(*arg, unsigned int);
	ret = ft_itoa_base_up(val, 16);
	ft_putstr(ret);
	ret_val = ft_strlen(ret);
	free(ret);
	return (ret_val);
}
